# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _empirical_orthogonal_function.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_empirical_orthogonal_function', [dirname(__file__)])
        except ImportError:
            import _empirical_orthogonal_function
            return _empirical_orthogonal_function
        if fp is not None:
            try:
                _mod = imp.load_module('_empirical_orthogonal_function', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _empirical_orthogonal_function = swig_import_helper()
    del swig_import_helper
else:
    import _empirical_orthogonal_function
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


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


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



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
except:
    weakref_proxy = lambda x: x



_empirical_orthogonal_function.SHARED_PTR_DISOWN_swigconstant(_empirical_orthogonal_function)
SHARED_PTR_DISOWN = _empirical_orthogonal_function.SHARED_PTR_DISOWN

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

import full_physics_swig.sub_state_vector_array
import full_physics_swig.generic_object
import full_physics_swig.instrument_correction
class EmpiricalOrthogonalFunction(full_physics_swig.instrument_correction.SubStateVectorArrayInstrumentCorrection):
    """

    This class applies a empirical orthogonal function (EOF) correction to
    instrument data.

    We use a supplied waveform, multiple by a single scale factor given by
    the state vector, and add this to the radiance calculated in
    InstrumentIls.

    Note that other than what we call this and there various metadata
    fields, this is the same thing as the ZeroOffsetWaveform.

    C++ includes: empirical_orthogonal_function.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def _v_eof(self):
        """

        ArrayWithUnit<double, 1> FullPhysics::EmpiricalOrthogonalFunction::eof() const
        Current value of empirical orthogonal function, for each pixel number.

        """
        return _empirical_orthogonal_function.EmpiricalOrthogonalFunction__v_eof(self)


    @property
    def eof(self):
        return self._v_eof()


    def _v_order(self):
        """

        int FullPhysics::EmpiricalOrthogonalFunction::order() const
        Order of the empirical orthogonal function (e.g., first order, second
        order, etc.) 
        """
        return _empirical_orthogonal_function.EmpiricalOrthogonalFunction__v_order(self)


    @property
    def order(self):
        return self._v_order()

    __swig_destroy__ = _empirical_orthogonal_function.delete_EmpiricalOrthogonalFunction
EmpiricalOrthogonalFunction._v_eof = new_instancemethod(_empirical_orthogonal_function.EmpiricalOrthogonalFunction__v_eof, None, EmpiricalOrthogonalFunction)
EmpiricalOrthogonalFunction._v_order = new_instancemethod(_empirical_orthogonal_function.EmpiricalOrthogonalFunction__v_order, None, EmpiricalOrthogonalFunction)
EmpiricalOrthogonalFunction_swigregister = _empirical_orthogonal_function.EmpiricalOrthogonalFunction_swigregister
EmpiricalOrthogonalFunction_swigregister(EmpiricalOrthogonalFunction)



