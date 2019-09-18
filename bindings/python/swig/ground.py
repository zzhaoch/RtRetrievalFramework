# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ground.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ground')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ground')
    _ground = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ground', [dirname(__file__)])
        except ImportError:
            import _ground
            return _ground
        try:
            _mod = imp.load_module('_ground', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ground = swig_import_helper()
    del swig_import_helper
else:
    import _ground
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


SHARED_PTR_DISOWN = _ground.SHARED_PTR_DISOWN

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

import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class ObservableGround(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ground.delete_ObservableGround
ObservableGround.add_observer_and_keep_reference = new_instancemethod(_ground.ObservableGround_add_observer_and_keep_reference, None, ObservableGround)
ObservableGround.add_observer = new_instancemethod(_ground.ObservableGround_add_observer, None, ObservableGround)
ObservableGround.remove_observer = new_instancemethod(_ground.ObservableGround_remove_observer, None, ObservableGround)
ObservableGround_swigregister = _ground.ObservableGround_swigregister
ObservableGround_swigregister(ObservableGround)

class ObserverGround(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _ground.ObserverGround_swiginit(self, _ground.new_ObserverGround())
    __swig_destroy__ = _ground.delete_ObserverGround
ObserverGround.notify_update = new_instancemethod(_ground.ObserverGround_notify_update, None, ObserverGround)
ObserverGround.notify_add = new_instancemethod(_ground.ObserverGround_notify_add, None, ObserverGround)
ObserverGround.notify_remove = new_instancemethod(_ground.ObserverGround_notify_remove, None, ObserverGround)
ObserverGround_swigregister = _ground.ObserverGround_swigregister
ObserverGround_swigregister(ObserverGround)

class Ground(ObservableGround):
    """

    This class maintains the ground portion of the state.

    Other objects may depend on the ground, and should be updated when the
    ground is updated. To facilitate that, this class in an Oberverable,
    and objects can add themselves as Observers to be notified when the
    ground is updated.

    This class is unfortunately a bit hard coded. The surface types are
    one of a set of enumerations. The surface parameters depend on exactly
    what the surface type is. These types and parameters map to types and
    parameters found in the LIDORT and LRAD code, so the hard coding is
    intrinsic.

    C++ includes: ground.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ground.delete_Ground

    def surface_parameter(self, wn, spec_index):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ground::surface_parameter(const double wn, const int spec_index) const =0
        Surface parmeters.

        What exactly these parameters mean is determined by the surface type,
        see the discussion in the comments before the Ground class. 
        """
        return _ground.Ground_surface_parameter(self, wn, spec_index)


    def clone(self):
        """

        virtual boost::shared_ptr<Ground> FullPhysics::Ground::clone() const =0
        Clone a Ground object.

        Note that the cloned version will not be attached to a StateVector,
        although you can of course attach them after receiving the cloned
        object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" Ground object. 
        """
        return _ground.Ground_clone(self)

Ground.__str__ = new_instancemethod(_ground.Ground___str__, None, Ground)
Ground.surface_parameter = new_instancemethod(_ground.Ground_surface_parameter, None, Ground)
Ground.clone = new_instancemethod(_ground.Ground_clone, None, Ground)
Ground.print_desc = new_instancemethod(_ground.Ground_print_desc, None, Ground)
Ground_swigregister = _ground.Ground_swigregister
Ground_swigregister(Ground)

class SubStateVectorArrayGround(Ground, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ground.delete_SubStateVectorArrayGround

    @property
    def coefficient(self):
        return self._v_coefficient()


    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayGround.init = new_instancemethod(_ground.SubStateVectorArrayGround_init, None, SubStateVectorArrayGround)
SubStateVectorArrayGround.state_vector_name_i = new_instancemethod(_ground.SubStateVectorArrayGround_state_vector_name_i, None, SubStateVectorArrayGround)
SubStateVectorArrayGround.update_sub_state_hook = new_instancemethod(_ground.SubStateVectorArrayGround_update_sub_state_hook, None, SubStateVectorArrayGround)
SubStateVectorArrayGround._v_coefficient = new_instancemethod(_ground.SubStateVectorArrayGround__v_coefficient, None, SubStateVectorArrayGround)
SubStateVectorArrayGround._v_used_flag_value = new_instancemethod(_ground.SubStateVectorArrayGround__v_used_flag_value, None, SubStateVectorArrayGround)
SubStateVectorArrayGround._v_statevector_covariance = new_instancemethod(_ground.SubStateVectorArrayGround__v_statevector_covariance, None, SubStateVectorArrayGround)
SubStateVectorArrayGround._v_pressure = new_instancemethod(_ground.SubStateVectorArrayGround__v_pressure, None, SubStateVectorArrayGround)
SubStateVectorArrayGround_swigregister = _ground.SubStateVectorArrayGround_swigregister
SubStateVectorArrayGround_swigregister(SubStateVectorArrayGround)



