# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ils.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ils')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ils')
    _ils = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ils', [dirname(__file__)])
        except ImportError:
            import _ils
            return _ils
        try:
            _mod = imp.load_module('_ils', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ils = swig_import_helper()
    del swig_import_helper
else:
    import _ils
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ils.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_ils.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_ils.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_ils.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_ils.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_ils.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_ils.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_ils.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_ils.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_ils.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_ils.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_ils.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_ils.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_ils.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_ils.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_ils.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_ils.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _ils.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _ils.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.state_vector
import full_physics_swig.generic_object
class Ils(full_physics_swig.state_vector.StateVectorObserver):
    """

    This class models an Instrument Line Shape (ILS).

    We convolve with high resolution data to produce a model of what we
    expect to observe in the Level 1b data.

    C++ includes: ils.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ils.delete_Ils

    def apply_ils(self, *args):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ils::apply_ils(const blitz::Array< double, 1 > &High_resolution_wave_number, const
        ArrayAd< double, 1 > &High_resolution_radiance, const std::vector< int
        > &Pixel_list) const =0
        Apply the ILS.

        This includes propagating the Jacobian from the high resolution data,
        and adding in any dependence of the ILS on the state vector elements
        (e.g., dispersion state vector elements).

        Parameters:
        -----------

        High_resolution_wave_number:  The wave numbers going with the high
        resolution radiance data. This is in cm^-1, and should be ordered from
        smallest to largest wavenumber.

        High_resolution_radiance:  The high resolution radiance data and
        jacobian . This is in w/m^2 / sr / cm^-1

        Pixel_list:  List of instrument pixels to include in the results. The
        order of the pixels is the same order that we return our results in.

        Radiance with ILS applied, and Jacobian This is in w/m^2 / sr / cm^-1.

        """
        return _ils.Ils_apply_ils(self, *args)


    def clone(self):
        """

        virtual boost::shared_ptr<Ils> FullPhysics::Ils::clone() const =0
        Clone an Ils object.

        Note that the cloned version will not be attached to and StateVector
        or Observer<Ils>, although you can of course attach them after
        receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" Ils object. 
        """
        return _ils.Ils_clone(self)


    def _v_band_name(self):
        """

        virtual std::string FullPhysics::Ils::band_name() const =0
        Descriptive name of the band. 
        """
        return _ils.Ils__v_band_name(self)


    @property
    def band_name(self):
        return self._v_band_name()


    def _v_hdf_band_name(self):
        """

        virtual std::string FullPhysics::Ils::hdf_band_name() const
        In general, the name used in HDF files for a particular band is
        similar but not identical to the more human readable band_name.

        For example, with GOSAT we use the HDF field name "weak_co2", but
        the band name is "WC-Band". This gives the HDF name to use.

        The default implementation just returns the same string as the band
        name. 
        """
        return _ils.Ils__v_hdf_band_name(self)


    @property
    def hdf_band_name(self):
        return self._v_hdf_band_name()


    def _v_pixel_grid(self):
        """

        virtual SpectralDomain FullPhysics::Ils::pixel_grid() const =0
        This is the pixel grid for each pixel. 
        """
        return _ils.Ils__v_pixel_grid(self)


    @property
    def pixel_grid(self):
        return self._v_pixel_grid()


    def _v_ils_half_width(self, *args):
        """

        virtual void FullPhysics::Ils::ils_half_width(const DoubleWithUnit &half_width)=0
        Set the half width of the ILS. 
        """
        return _ils.Ils__v_ils_half_width(self, *args)


    @property
    def ils_half_width(self):
        return self._v_ils_half_width()

    @ils_half_width.setter
    def ils_half_width(self, value):
      self._v_ils_half_width(value)

Ils.__str__ = new_instancemethod(_ils.Ils___str__, None, Ils)
Ils.apply_ils = new_instancemethod(_ils.Ils_apply_ils, None, Ils)
Ils.clone = new_instancemethod(_ils.Ils_clone, None, Ils)
Ils._v_band_name = new_instancemethod(_ils.Ils__v_band_name, None, Ils)
Ils._v_hdf_band_name = new_instancemethod(_ils.Ils__v_hdf_band_name, None, Ils)
Ils._v_pixel_grid = new_instancemethod(_ils.Ils__v_pixel_grid, None, Ils)
Ils._v_ils_half_width = new_instancemethod(_ils.Ils__v_ils_half_width, None, Ils)
Ils_swigregister = _ils.Ils_swigregister
Ils_swigregister(Ils)

class vector_ils(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _ils.vector_ils_swiginit(self, _ils.new_vector_ils(*args))
    __swig_destroy__ = _ils.delete_vector_ils
vector_ils.iterator = new_instancemethod(_ils.vector_ils_iterator, None, vector_ils)
vector_ils.__nonzero__ = new_instancemethod(_ils.vector_ils___nonzero__, None, vector_ils)
vector_ils.__bool__ = new_instancemethod(_ils.vector_ils___bool__, None, vector_ils)
vector_ils.__len__ = new_instancemethod(_ils.vector_ils___len__, None, vector_ils)
vector_ils.__getslice__ = new_instancemethod(_ils.vector_ils___getslice__, None, vector_ils)
vector_ils.__setslice__ = new_instancemethod(_ils.vector_ils___setslice__, None, vector_ils)
vector_ils.__delslice__ = new_instancemethod(_ils.vector_ils___delslice__, None, vector_ils)
vector_ils.__delitem__ = new_instancemethod(_ils.vector_ils___delitem__, None, vector_ils)
vector_ils.__getitem__ = new_instancemethod(_ils.vector_ils___getitem__, None, vector_ils)
vector_ils.__setitem__ = new_instancemethod(_ils.vector_ils___setitem__, None, vector_ils)
vector_ils.pop = new_instancemethod(_ils.vector_ils_pop, None, vector_ils)
vector_ils.append = new_instancemethod(_ils.vector_ils_append, None, vector_ils)
vector_ils.empty = new_instancemethod(_ils.vector_ils_empty, None, vector_ils)
vector_ils.size = new_instancemethod(_ils.vector_ils_size, None, vector_ils)
vector_ils.swap = new_instancemethod(_ils.vector_ils_swap, None, vector_ils)
vector_ils.begin = new_instancemethod(_ils.vector_ils_begin, None, vector_ils)
vector_ils.end = new_instancemethod(_ils.vector_ils_end, None, vector_ils)
vector_ils.rbegin = new_instancemethod(_ils.vector_ils_rbegin, None, vector_ils)
vector_ils.rend = new_instancemethod(_ils.vector_ils_rend, None, vector_ils)
vector_ils.clear = new_instancemethod(_ils.vector_ils_clear, None, vector_ils)
vector_ils.get_allocator = new_instancemethod(_ils.vector_ils_get_allocator, None, vector_ils)
vector_ils.pop_back = new_instancemethod(_ils.vector_ils_pop_back, None, vector_ils)
vector_ils.erase = new_instancemethod(_ils.vector_ils_erase, None, vector_ils)
vector_ils.push_back = new_instancemethod(_ils.vector_ils_push_back, None, vector_ils)
vector_ils.front = new_instancemethod(_ils.vector_ils_front, None, vector_ils)
vector_ils.back = new_instancemethod(_ils.vector_ils_back, None, vector_ils)
vector_ils.assign = new_instancemethod(_ils.vector_ils_assign, None, vector_ils)
vector_ils.resize = new_instancemethod(_ils.vector_ils_resize, None, vector_ils)
vector_ils.insert = new_instancemethod(_ils.vector_ils_insert, None, vector_ils)
vector_ils.reserve = new_instancemethod(_ils.vector_ils_reserve, None, vector_ils)
vector_ils.capacity = new_instancemethod(_ils.vector_ils_capacity, None, vector_ils)
vector_ils_swigregister = _ils.vector_ils_swigregister
vector_ils_swigregister(vector_ils)



