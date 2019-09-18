/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.12
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_luabind_object_WRAP_H_
#define SWIG_luabind_object_WRAP_H_

#include <map>
#include <string>


class SwigDirector_LuaCallback : public FullPhysics::LuaCallback, public Swig::Director {

public:
    SwigDirector_LuaCallback(PyObject *self, FullPhysics::LuaState const &Ls);
    virtual ~SwigDirector_LuaCallback();
    virtual boost::shared_ptr< FullPhysics::LuabindObject > call(boost::shared_ptr< FullPhysics::LuabindObject > const &Obj1, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj2, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj3, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj4, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj5, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj6, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj7, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj8, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj9, boost::shared_ptr< FullPhysics::LuabindObject > const &Obj10);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class LuaCallback doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[1];
#endif

};


#endif
