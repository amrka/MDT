import warnings

import six

from mdt.component_templates.base import ComponentBuilder, method_binding_meta, ComponentTemplate
from mdt.components import has_component, get_component
from mot.cl_data_type import SimpleCLDataType
from mdt.model_building.parameter_functions.numdiff_info import NumDiffInfo, SimpleNumDiffInfo
from mdt.model_building.parameters import ProtocolParameter, FreeParameter
from mdt.model_building.parameter_functions.priors import UniformWithinBoundsPrior
from mdt.model_building.parameter_functions.transformations import AbstractTransformation


__author__ = 'Robbert Harms'
__date__ = "2015-12-12"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class ParameterBuilder(ComponentBuilder):

    def create_class(self, template):
        """Creates classes with as base class DMRICompositeModel

        Args:
            template (Type[ParameterTemplate]): the configuration for the parameter.
        """
        data_type = template.data_type
        if isinstance(data_type, six.string_types):
            data_type = SimpleCLDataType.from_string(data_type)

        # todo remove in future versions
        if issubclass(template, StaticMapParameterTemplate):
            warnings.warn('"StaticMapParameterTemplate" are deprecated in favor of "ProtocolParameterTemplate" '
                          'and will be removed in future versions.')

        if issubclass(template, ProtocolParameterTemplate):
            class AutoProtocolParameter(method_binding_meta(template, ProtocolParameter)):
                def __init__(self, nickname=None):
                    super(AutoProtocolParameter, self).__init__(data_type, nickname or template.name,
                                                                value=template.value)
            return AutoProtocolParameter

        elif issubclass(template, FreeParameterTemplate):
            numdiff_info = template.numdiff_info
            if not isinstance(numdiff_info, NumDiffInfo) and numdiff_info is not None:
                numdiff_info = SimpleNumDiffInfo(**numdiff_info)

            class AutoFreeParameter(method_binding_meta(template, FreeParameter)):
                def __init__(self, nickname=None):
                    super(AutoFreeParameter, self).__init__(
                        data_type,
                        nickname or template.name,
                        template.fixed,
                        template.init_value,
                        template.lower_bound,
                        template.upper_bound,
                        parameter_transform=_resolve_parameter_transform(template.parameter_transform),
                        sampling_proposal_std=template.sampling_proposal_std,
                        sampling_prior=template.sampling_prior,
                        numdiff_info=numdiff_info
                    )
                    self.sampling_proposal_modulus = template.sampling_proposal_modulus
            return AutoFreeParameter


class ParameterTemplate(ComponentTemplate):
    """The cascade template to inherit from.

    These templates are loaded on the fly by the ParametersBuilder

    template options:
        name (str): the name of the parameter, defaults to the class name
        description (str): the description of this parameter
        data_type (str or DataType): either a string we use as datatype or the actual datatype itself
    """
    _component_type = 'parameters'
    _builder = ParameterBuilder()

    name = ''
    description = ''
    data_type = 'mot_float_type'


class ProtocolParameterTemplate(ParameterTemplate):
    """The default template options for protocol parameters.
    """
    data_type = 'mot_float_type'
    value = None


# Todo: deprecate and remove in future versions
class StaticMapParameterTemplate(ProtocolParameterTemplate):
    pass


class FreeParameterTemplate(ParameterTemplate):
    """The default template options for free parameters.

    Attributes:
        init_value (float): the initial value
        fixed (boolean or ndarray of float): if this parameter is fixed or not. If not fixed this should
            hold a reference to a value or a matrix
        lower_bound (float): the lower bounds
        upper_bound (float): the upper bounds
        parameter_transform
            (str or :class:`~mdt.model_building.parameter_functions.transformations.AbstractTransformation`): the
            parameter transformation, this is used for automatic range transformation of the parameters during
            optimization. See Harms 2017 NeuroImage for details. Typical elements are:

            * ``Identity``: no transformation
            * ``Positivity``: ensures the parameters are positive
            * ``Clamp``: limits the parameter between its lower and upper bounds
            * ``CosSqrClamp``: changes the range of the optimized parameters to [0, 1] and ensures boundary constraints
            * ``SinSqrClamp``: same as ``CosSqrClamp``
            * ``SqrClamp``: same as clamp but with an additional square root to change the magnitude of the range
            * ``AbsModPi``: ensures absolute modulus of the input parameters between zero and pi.
            * ``AbsModTwoPi``: ensures absolute modulus of the input parameters between zero and two pi.

        sampling_proposal_std (float): the default proposal standard deviation for this parameter. This is used
            in some MCMC sampling routines.
        sampling_proposal_modulus (float or None): if given, a modulus we will use when finalizing the proposal
            distributions. That is, when we are finalizing the proposals we will take, if set, the absolute
            modulus of that parameter to ensure the parameter is within [0, <modulus>].
        sampling_prior: the prior function
        numdiff_info (dict or :class:`~mdt.model_building.parameter_functions.numdiff_info.NumDiffInfo`):
            the information necessary to take the numerical derivative of a model with respect to this parameter.
            Either a dictionary with the keyword arguments to
            :class:`~mdt.model_building.parameter_functions.numdiff_info.SimpleNumDiffInfo` or an information
            object directly. If None, we use an empty dictionary. Please note that if you override this, you will have
            to specify all of the items (no automatic inheritance of sub-items).
    """
    data_type = 'mot_float_type'
    fixed = False
    init_value = 0.03
    lower_bound = 0.0
    upper_bound = 4.0
    parameter_transform = 'Identity'
    sampling_proposal_std = 1
    sampling_proposal_modulus = None
    sampling_prior = UniformWithinBoundsPrior()
    numdiff_info = {'max_step': 0.1, 'scale_factor': 1, 'use_bounds': True, 'modulus': None,
                    'use_upper_bound': True, 'use_lower_bound': True}


def _resolve_parameter_transform(parameter_transform):
    """Resolves input parameter transforms to actual objects.

    Args:
        parameter_transform
            (str or :class:`~mdt.model_building.parameter_functions.transformations.AbstractTransformation`):
            a parameter transformation name (with or without the postfix ``Transform``) or an actual object we
            just return.

    Returns:
        mdt.model_building.parameter_functions.transformations.AbstractTransformation: an actual transformation object

    Raises:
        ValueError: if the parameter transformation could not be resolved.
    """
    if isinstance(parameter_transform, AbstractTransformation):
        return parameter_transform

    if has_component('parameter_transforms', parameter_transform):
        return get_component('parameter_transforms', parameter_transform)()

    if has_component('parameter_transforms', parameter_transform + 'Transform'):
        return get_component('parameter_transforms', parameter_transform + 'Transform')()

    raise ValueError('Could not resolve the parameter transformation "{}"'.format(parameter_transform))
