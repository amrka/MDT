import glob
import warnings
import numpy as np
import yaml
import matplotlib.font_manager
import mdt
import mdt.visualization.layouts
from mdt.visualization.dict_conversion import StringConversion, \
    SimpleClassConversion, IntConversion, SimpleListConversion, BooleanConversion, \
    ConvertDictElements, ConvertDynamicFromModule, FloatConversion
from mdt.visualization.layouts import Rectangular

__author__ = 'Robbert Harms'
__date__ = "2016-09-02"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class MapPlotConfig(object):

    def __init__(self, dimension=2, slice_index=0, volume_index=0, rotate=0, colormap='hot', maps_to_show=(),
                 font=None, grid_layout=None, colorbar_nmr_ticks=10, show_axis=True, zoom=None,
                 map_plot_options=None):
        """Container for all plot related settings.

        Args:
            dimension (int): the dimension we are viewing
            slice_index (int): the slice in the dimension we are viewing
            volume_index (int): in the case of multiple volumes (4th dimension) which index we are in.
            rotate (int): the rotation factor, multiple of 90
            colormap (str): the name of the colormap to use
            maps_to_show (list of str): the names of the maps to show
            font (int): the font settings
            grid_layout (GridLayout): the layout of the grid
            colorbar_nmr_ticks (int): the number of ticks on the colorbar
            show_axis (bool): if we show the axis or not
            zoom (Zoom): the zoom setting for all the plots
            map_plot_options (dict): per map the map specific plot options
        """
        super(MapPlotConfig, self).__init__()
        self.dimension = dimension
        self.slice_index = slice_index
        self.volume_index = volume_index
        self.rotate = rotate
        self.colormap = colormap
        self.maps_to_show = maps_to_show
        self.zoom = zoom or Zoom(Point(0, 0), Point(0, 0))
        self.font = font or Font()
        self.colorbar_nmr_ticks = colorbar_nmr_ticks
        self.show_axis = show_axis
        self.map_plot_options = map_plot_options or {}
        self.grid_layout = grid_layout or Rectangular()

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        return {'dimension': IntConversion(),
                'slice_index': IntConversion(),
                'volume_index': IntConversion(),
                'rotate': IntConversion(),
                'colormap': StringConversion(),
                'maps_to_show': SimpleListConversion(),
                'zoom': Zoom.get_conversion_info(),
                'font': Font.get_conversion_info(),
                'colorbar_nmr_ticks': IntConversion(),
                'show_axis': BooleanConversion(),
                'map_plot_options': ConvertDictElements(SingleMapConfig.get_conversion_info()),
                'grid_layout': ConvertDynamicFromModule(mdt.visualization.layouts)
                }

    @classmethod
    def from_yaml(cls, text):
        return cls.get_conversion_info().from_dict(yaml.load(text))

    @classmethod
    def from_dict(cls, config_dict):
        return cls.get_conversion_info().from_dict(config_dict)

    def get_rotation(self):
        """Get the rotation we would like to apply on the configuration.

        This can differ from the instance variable rotate. The instance variable is what the user set,
        this function returns what we make of it.

        Returns:
            int: a angle as multiple of 90, can be negative.
        """
        return -self.rotate - 90

    def to_dict(self):
        return self.get_conversion_info().to_dict(self)

    def to_yaml(self):
        return yaml.safe_dump(self.get_conversion_info().to_dict(self))

    def __repr__(self):
        return str(self.get_conversion_info().to_dict(self))

    def __eq__(self, other):
        if not isinstance(other, MapPlotConfig):
            return NotImplemented
        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class SingleMapConfig(object):

    def __init__(self, title=None, scale=None, clipping=None, colormap=None, colorbar_label=None):
        super(SingleMapConfig, self).__init__()
        self.title = title
        self.scale = scale or Scale()
        self.clipping = clipping or Clipping()
        self.colormap = colormap
        self.colorbar_label = colorbar_label

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        return {'title': StringConversion(),
                'scale': Scale.get_conversion_info(),
                'clipping': Clipping.get_conversion_info(),
                'colormap': StringConversion(),
                'colorbar_label': StringConversion()}

    @classmethod
    def from_yaml(cls, text):
        return cls.get_conversion_info().from_dict(yaml.load(text))

    @classmethod
    def from_dict(cls, config_dict):
        return cls.get_conversion_info().from_dict(config_dict)

    def to_dict(self):
        return self.get_conversion_info().to_dict(self)

    def to_yaml(self):
        return yaml.safe_dump(self.get_conversion_info().to_dict(self))

    def __repr__(self):
        return str(self.get_conversion_info().to_dict(self))

    def __eq__(self, other):
        if not isinstance(other, SingleMapConfig):
            return NotImplemented

        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Zoom(object):

    def __init__(self, p0, p1):
        """Container for zooming a map between the two given points.

        Args:
            p0 (Point): the lower left corner of the zoomed area
            p1 (Point): the upper right corner of the zoomed area
        """
        self.p0 = p0
        self.p1 = p1

    @classmethod
    def no_zoom(cls):
        return cls(Point(0, 0), Point(0, 0))

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        point_converter = Point.get_conversion_info()
        return {'p0': point_converter,
                'p1': point_converter}

    def apply(self, data):
        """Apply the zoom to the given 2d array and return the new array.

        Args:
           data (ndarray): the data to zoom in on
        """
        correct = self.p0.x < data.shape[1] and self.p1.x < data.shape[1] \
                  and self.p0.y < data.shape[0] and self.p1.y < data.shape[0] \
                  and self.p0.x < self.p1.x and self.p0.y < self.p1.y
        if correct:
            return data[self.p0.y:self.p1.y, self.p0.x:self.p1.x]
        return data
    #
    # def rotate(self, rotate, max_x, max_y):
    #todo
    #     """Rotate this zoom box around a 90 degree angle.
    #
    #     Args:
    #         rotate (int): the angle around which to rotate, one of 0, 90, 180, 270.
    #         max_x (int): the (not rotated) maximum x index
    #         max_y (int): the (not rotated) maximum y index
    #
    #     Returns:
    #         Zoom: the rotated zoom box
    #     """
    #     # if rotate == 90:
    #     #     return Zoom(Point(self.p0.y, self.p1.x).rotate(rotate, max_x, max_y),
    #     #                 Point(self.p1.y, self.p0.x).rotate(rotate, max_x, max_y))
    #
    #     return self

    def __repr__(self):
        return str(self.get_conversion_info().to_dict(self))

    def __eq__(self, other):
        if not isinstance(other, Zoom):
            return NotImplemented

        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Point(object):

    def __init__(self, x, y):
        """Container for a single point"""
        self.x = x
        self.y = y

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        return {'x': IntConversion(),
                'y': IntConversion()}

    def rotated(self, rotate, shape):
        """Rotate this point around a 90 degree angle and translate the results to a new origin.

        This uses the given maximum (x, y) of the non-rotated 2d image to translate the results.

        Args:
            rotate (int): the angle around which to rotate, one of 0, 90, 180, 270.
            shape (tuple): the shape of the complete area, (max_x, max_y)

        Returns:
            Point: the rotated point
        """
        return Point(*self._rotate_coordinate(self.x, self.y, rotate, shape))

    def _rotate_coordinate(self, x, y, rotate, shape):
        positive_number_of_90deg_rotations = (rotate % 360) // 90

        rx, ry = x, y
        for rotation in range(1, positive_number_of_90deg_rotations + 1):
            # apply rotation and translate on the x component
            current_max_x, current_max_y = np.roll(shape, rotation)
            rx, ry = current_max_y - ry, rx
        return rx, ry

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Clipping(object):

    def __init__(self, vmin=0, vmax=0, use_min=False, use_max=False):
        """Container for the map clipping information"""
        self.vmin = vmin
        self.vmax = vmax
        self.use_min = use_min
        self.use_max = use_max

    def apply(self, data):
        """Apply the clipping to the given 2d array and return the new array.

        Args:
           data (ndarray): the data to clip
        """
        if self.use_max or self.use_min:
            clipping_min = data.min()
            if self.use_min:
                clipping_min = self.vmin

            clipping_max = data.max()
            if self.use_max:
                clipping_max = self.vmax

            return np.clip(data, clipping_min, clipping_max)

        return data

    def get_updated(self, **kwargs):
        """Get a new Clipping object with updated arguments.

        Args:
            **kwargs (dict): the new keyword values, when given these take precedence over the current ones.

        Returns:
            Clipping: a new scale with updated values.
        """
        new_values = dict(vmin=self.vmin, vmax=self.vmax, use_min=self.use_min, use_max=self.use_max)
        new_values.update(**kwargs)
        return Clipping(**new_values)

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        return {'vmax': FloatConversion(allow_null=False),
                'vmin': FloatConversion(allow_null=False),
                'use_min': BooleanConversion(allow_null=False),
                'use_max': BooleanConversion(allow_null=False)}

    def __eq__(self, other):
        if not isinstance(other, Clipping):
            return NotImplemented

        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Scale(object):

    def __init__(self, vmin=0, vmax=0, use_min=False, use_max=False):
        """Container the map scaling information"""
        self.vmin = vmin
        self.vmax = vmax
        self.use_min = use_min
        self.use_max = use_max

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        return {'vmax': FloatConversion(allow_null=False),
                'vmin': FloatConversion(allow_null=False),
                'use_min': BooleanConversion(allow_null=False),
                'use_max': BooleanConversion(allow_null=False)}

    def get_updated(self, **kwargs):
        """Get a new Scale object with updated arguments.

        Args:
            **kwargs (dict): the new keyword values, when given these take precedence over the current ones.

        Returns:
            Scale: a new scale with updated values.
        """
        new_values = dict(vmin=self.vmin, vmax=self.vmax, use_min=self.use_min, use_max=self.use_max)
        new_values.update(**kwargs)
        return Scale(**new_values)

    def __eq__(self, other):
        if not isinstance(other, Scale):
            return NotImplemented

        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Font(object):

    def __init__(self, family='sans-serif', size=14):
        """Information about the font to use

        Args:
            name: the name of the font to use
            size: the size of the font (> 0).
        """
        self.family = family
        self.size = size

        if family not in self.font_names():
            raise ValueError("The given font \"{}\" is not recognized.".format(family))
        if size < 1:
            raise ValueError("The size ({}) can not be smaller than 1".format(str(size)))

    @property
    def name(self):
        return self.family

    @classmethod
    def font_names(cls):
        """Get the name of supported fonts

        Returns:
            list of str: the name of the supported fonts and font families.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fonts = matplotlib.font_manager.get_fontconfig_fonts()
            names = [matplotlib.font_manager.FontProperties(fname=font_name).get_name() for font_name in fonts]
        return list(sorted(['sans-serif', 'serif', 'cursive', 'fantasy', 'monospace'])) + list(sorted(names))

    @classmethod
    def get_conversion_info(cls):
        return SimpleClassConversion(cls, cls._get_attribute_conversions())

    @classmethod
    def _get_attribute_conversions(cls):
        return {'family': StringConversion(),
                'size': IntConversion()}

    def __eq__(self, other):
        if not isinstance(other, Font):
            return NotImplemented

        for key, value in self.__dict__.items():
            if value != getattr(other, key):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class DataInfo(object):

    def __init__(self, maps, directory=None):
        """A container for basic information about the volume maps we are viewing.

        Args:
            maps (dict): the dictionary with the maps to view
            directory (str): the directory from which the maps where loaded
        """
        self.maps = maps
        self.directory = directory
        self.map_info = {key: SingleMapInfo(key, value) for key, value in self.maps.items()}
        self.sorted_keys = list(sorted(maps.keys()))

    @classmethod
    def from_dir(cls, directory):
        if directory is None:
            return cls({}, None)
        return cls(mdt.load_volume_maps(directory), directory)

    def get_file_name(self, map_name):
        """Get the file name of the given map

        Returns:
            None if the map could not be found on dir, else a string with the file path.
        """
        if not self.directory:
            return None

        items = list(glob.glob(self.directory + '/{}.nii*'.format(map_name)))
        if items:
            return items[0]

        return None

    def get_max_dimension(self, map_names=None):
        """Get the maximum dimension index in the maps.

        Args:
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            int: either, 0, 1, 2 as the maximum dimension index in the maps.
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        return max(self.map_info[map_name].max_dimension() for map_name in map_names)

    def get_max_slice_index(self, dimension, map_names=None):
        """Get the maximum slice index in the given map on the given dimension.

        Args:
            dimension (int): the dimension we want the slice index of (maximum 3)
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            int: the maximum slice index over the given maps in the given dimension.
        """
        max_dimension = self.get_max_dimension(map_names)
        if not map_names:
            raise ValueError('No maps to search in.')
        if dimension > max_dimension:
            raise ValueError('Dimension can not exceed {}.'.format(max_dimension))
        return max(self.map_info[map_name].max_slice_index(dimension) for map_name in map_names)

    def get_max_volume_index(self, map_names=None):
        """Get the maximum volume index in the given maps.

        Args:
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            int: the maximum volume index in the given list of maps. Starts from 0.
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        return max(self.map_info[map_name].max_volume_index() for map_name in map_names)

    def get_index_first_non_zero_slice(self, dimension, map_names=None):
        """Get the index of the first non zero slice in the maps.

        Args:
            dimension (int): the dimension to search in
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            int: the slice index with the first non zero values.
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        for map_name in map_names:
            index = self.map_info[map_name].get_index_first_non_zero_slice(dimension)
            if index is not None:
                return index
        return 0

    def slice_has_data(self, dimension, slice_index, map_names=None):
        """Check if at least one of the maps has non zero numbers on the given slice.

        Args:
            dimension (int): the dimension to search in
            slice_index (int): the index of the slice in the given dimension
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            bool: true if at least on of the maps has data in the given slice
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        for map_name in map_names:
            if self.map_info[map_name].slice_has_data(dimension, slice_index):
                return True
        return False

    def get_max_x(self, dimension, rotate=0, map_names=None):
        """Get the maximum x index supported over the images.

        In essence this gets the lowest x index found.

        Args:
            dimension (int): the dimension to search in
            rotate (int): the rotation factor by which we rotate the slices within the given dimension
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            int: the maximum x-index found.
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        return min(self.map_info[map_name].get_max_x(dimension, rotate) for map_name in map_names)

    def get_max_y(self, dimension, rotate=0, map_names=None):
        """Get the maximum y index supported over the images.

        In essence this gets the lowest y index found.

        Args:
            dimension (int): the dimension to search in
            rotate (int): the rotation factor by which we rotate the slices within the given dimension
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            int: the maximum y-index found.
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        return min(self.map_info[map_name].get_max_y(dimension, rotate) for map_name in map_names)

    def get_bounding_box(self, dimension, slice_index, volume_index, rotate, map_names=None):
        """Get the bounding box of the images.

        Args:
            dimension (int): the dimension to search in
            slice_index (int): the slice index in that dimension
            volume_index (int): the current volume index
            rotate (int): the angle by which to rotate the image before getting the bounding box
            map_names (list of str): if given we will only scan the given list of maps

        Returns:
            tuple of Point: two point designating first the upper left corner and second the lower right corner of the
                bounding box.
        """
        map_names = map_names or self.maps.keys()
        if not map_names:
            raise ValueError('No maps to search in.')
        bounding_boxes = [self.map_info[map_name].get_bounding_box(dimension, slice_index, volume_index, rotate)
                          for map_name in map_names]

        p0x = min([bbox[0].x for bbox in bounding_boxes])
        p0y = min([bbox[0].y for bbox in bounding_boxes])
        p1x = max([bbox[1].x for bbox in bounding_boxes])
        p1y = max([bbox[1].y for bbox in bounding_boxes])

        return Point(p0x, p0y), Point(p1x, p1y)


class SingleMapInfo(object):

    def __init__(self, map_name, data):
        """Holds information about a single map.

        Args:
            map_name (str): the name of the map
            data (ndarray): the value of the map
        """
        self.map_name = map_name
        self.data = data

    def max_dimension(self):
        """Get the maximum dimension index in this map.

        The maximum value returned by this method is 2 and the minimum is 0.

        Returns:
            int: in the range 0, 1, 2
        """
        return min(len(self.data.shape), 3) - 1

    def max_slice_index(self, dimension):
        """Get the maximum slice index on the given dimension.

        Args:
            dimension (int): the dimension we want the slice index of (maximum 3)

        Returns:
            int: the maximum slice index in the given dimension.
        """
        return self.data.shape[dimension] - 1

    def slice_has_data(self, dimension, slice_index):
        """Check if this map has non zero values in the given slice index.

        Args:
            dimension (int): the dimension we want the slice index of (maximum 3)
            slice_index (int): the slice index to look in

        Returns:
            int: the maximum slice index in the given dimension.
        """
        slice_indexing = [slice(None)] * (self.max_dimension() + 1)
        slice_indexing[dimension] = slice_index
        return np.count_nonzero(self.data[slice_indexing])

    def max_volume_index(self):
        """Get the maximum volume index in this map.

        The minimum is 0.

        Returns:
            int: the maximum volume index.
        """
        if len(self.data.shape) > 3:
            return self.data.shape[3] - 1
        return 0

    def get_index_first_non_zero_slice(self, dimension):
        """Get the index of the first non zero slice in this map.

        Args:
            dimension (int): the dimension to search in

        Returns:
            int: the slice index with the first non zero values.
        """
        slice_index = [slice(None)] * (self.max_dimension() + 1)
        for index in range(self.data.shape[dimension]):
            slice_index[dimension] = index
            if np.count_nonzero(self.data[slice_index]) > 0:
                return index
        return 0

    def get_max_x(self, dimension, rotate=0):
        """Get the maximum x index.

        Args:
            dimension (int): the dimension to search in
            rotate (int): the value by which to rotate the slices in the given dimension

        Returns:
            int: the maximum x index
        """
        shape = list(self.data.shape)[0:3]
        del shape[dimension]
        if rotate // 90 % 2 == 0:
            return max(0, shape[1] - 1)
        return max(0, shape[0] - 1)

    def get_max_y(self, dimension, rotate=0):
        """Get the maximum y index.

        Args:
            dimension (int): the dimension to search in
            rotate (int): the value by which to rotate the slices in the given dimension

        Returns:
            int: the maximum y index
        """
        shape = list(self.data.shape)[0:3]
        del shape[dimension]
        if rotate // 90 % 2 == 0:
            return max(0, shape[0] - 1)
        return max(0, shape[1] - 1)

    def get_size_in_dimension(self, dimension, rotate=0):
        """Get the shape of the 2d view on the data in the given dimension.

        This basically returns a pair of (max_x, max_y).

        Args:
            dimension (int): the dimension to search in
            rotate (int): the value by which to rotate the slices in the given dimension

        Returns:
            tuple: (max_x, max_y)
        """
        return self.get_max_x(dimension, rotate), self.get_max_y(dimension, rotate)

    def get_bounding_box(self, dimension, slice_index, volume_index, rotate):
        """Get the bounding box of this map when displayed using the given indicing.

        Args:
            dimension (int): the dimension to search in
            slice_index (int): the slice index in that dimension
            volume_index (int): the current volume index
            rotate (int): the angle by which to rotate the image before getting the bounding box

        Returns:
            tuple of Point: two point designating first the upper left corner and second the lower right corner of the
                bounding box.
        """
        def bbox(image):
            rows = np.any(image, axis=1)
            cols = np.any(image, axis=0)
            row_min, row_max = np.where(rows)[0][[0, -1]]
            column_min, column_max = np.where(cols)[0][[0, -1]]

            return row_min, row_max, column_min, column_max

        slice_indexing = [slice(None)] * (self.max_dimension() + 1)
        slice_indexing[dimension] = slice_index

        image = self.data[slice_indexing]

        if len(image.shape) > 2:
            if image.shape[2] > 1:
                image = image[..., volume_index]
            else:
                image = image[..., 0]

        if rotate:
            image = np.rot90(image, rotate // 90)

        row_min, row_max, column_min, column_max = bbox(image)

        return Point(column_min, row_min), Point(column_max, row_max)
