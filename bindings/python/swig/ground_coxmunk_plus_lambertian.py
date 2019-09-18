# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ground_coxmunk_plus_lambertian.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ground_coxmunk_plus_lambertian')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ground_coxmunk_plus_lambertian')
    _ground_coxmunk_plus_lambertian = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ground_coxmunk_plus_lambertian', [dirname(__file__)])
        except ImportError:
            import _ground_coxmunk_plus_lambertian
            return _ground_coxmunk_plus_lambertian
        try:
            _mod = imp.load_module('_ground_coxmunk_plus_lambertian', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ground_coxmunk_plus_lambertian = swig_import_helper()
    del swig_import_helper
else:
    import _ground_coxmunk_plus_lambertian
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


SHARED_PTR_DISOWN = _ground_coxmunk_plus_lambertian.SHARED_PTR_DISOWN

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

import full_physics_swig.ground
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.sub_state_vector_proxy
class GroundCoxmunkPlusLambertian(full_physics_swig.ground.Ground, full_physics_swig.sub_state_vector_proxy.SubStateVectorProxy):
    """

    This class implements a Coxmunk plus Lambertian ground type.

    C++ includes: ground_coxmunk_plus_lambertian.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Coxmunk, Lambertian):
        """

        GroundCoxmunkPlusLambertian::GroundCoxmunkPlusLambertian(const boost::shared_ptr< GroundCoxmunk > &Coxmunk, const
        boost::shared_ptr< GroundLambertian > &Lambertian)

        """
        _ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian_swiginit(self, _ground_coxmunk_plus_lambertian.new_GroundCoxmunkPlusLambertian(Coxmunk, Lambertian))

    def _v_coxmunk(self):
        """

        virtual const boost::shared_ptr<GroundCoxmunk> FullPhysics::GroundCoxmunkPlusLambertian::coxmunk() const

        """
        return _ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian__v_coxmunk(self)


    @property
    def coxmunk(self):
        return self._v_coxmunk()


    def _v_lambertian(self):
        """

        virtual const boost::shared_ptr<GroundLambertian> FullPhysics::GroundCoxmunkPlusLambertian::lambertian() const

        """
        return _ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian__v_lambertian(self)


    @property
    def lambertian(self):
        return self._v_lambertian()


    def desc(self):
        """

        virtual std::string FullPhysics::GroundCoxmunkPlusLambertian::desc() const

        """
        return _ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian_desc(self)

    __swig_destroy__ = _ground_coxmunk_plus_lambertian.delete_GroundCoxmunkPlusLambertian
GroundCoxmunkPlusLambertian._v_coxmunk = new_instancemethod(_ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian__v_coxmunk, None, GroundCoxmunkPlusLambertian)
GroundCoxmunkPlusLambertian._v_lambertian = new_instancemethod(_ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian__v_lambertian, None, GroundCoxmunkPlusLambertian)
GroundCoxmunkPlusLambertian.desc = new_instancemethod(_ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian_desc, None, GroundCoxmunkPlusLambertian)
GroundCoxmunkPlusLambertian_swigregister = _ground_coxmunk_plus_lambertian.GroundCoxmunkPlusLambertian_swigregister
GroundCoxmunkPlusLambertian_swigregister(GroundCoxmunkPlusLambertian)



