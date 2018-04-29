from mdt.component_templates.compartment_models import CompartmentTemplate

__author__ = 'Robbert Harms'
__date__ = "2015-06-21"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class CylinderGPD(CompartmentTemplate):

    parameters = ('g', 'G', 'Delta', 'delta', 'd', 'theta', 'phi', 'R')
    dependencies = ('MRIConstants',
                    'VanGelderenCylindricalRestrictedSignal',
                    'SphericalToCartesian')
    cl_code = '''
        mot_float_type b = pown(GAMMA_H * delta * G, 2) * (Delta - (delta/3.0));

        mot_float_type lperp = VanGelderenCylindricalRestrictedSignal(Delta, delta, d, R, G) / (G*G);

        mot_float_type gn2 = pown(dot(g, SphericalToCartesian(theta, phi)), 2);

        return exp( (lperp * (G*G - gn2)) + (-b * d * gn2));
    '''
