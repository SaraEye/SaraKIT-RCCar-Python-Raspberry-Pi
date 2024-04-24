# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sarakitdevices
else:
    import _sarakitdevices

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class InfoAccGyro(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    accX = property(_sarakitdevices.InfoAccGyro_accX_get, _sarakitdevices.InfoAccGyro_accX_set)
    accY = property(_sarakitdevices.InfoAccGyro_accY_get, _sarakitdevices.InfoAccGyro_accY_set)
    accZ = property(_sarakitdevices.InfoAccGyro_accZ_get, _sarakitdevices.InfoAccGyro_accZ_set)
    gyroX = property(_sarakitdevices.InfoAccGyro_gyroX_get, _sarakitdevices.InfoAccGyro_gyroX_set)
    gyroY = property(_sarakitdevices.InfoAccGyro_gyroY_get, _sarakitdevices.InfoAccGyro_gyroY_set)
    gyroZ = property(_sarakitdevices.InfoAccGyro_gyroZ_get, _sarakitdevices.InfoAccGyro_gyroZ_set)
    temp = property(_sarakitdevices.InfoAccGyro_temp_get, _sarakitdevices.InfoAccGyro_temp_set)
    rawAccX = property(_sarakitdevices.InfoAccGyro_rawAccX_get, _sarakitdevices.InfoAccGyro_rawAccX_set)
    rawAccY = property(_sarakitdevices.InfoAccGyro_rawAccY_get, _sarakitdevices.InfoAccGyro_rawAccY_set)
    rawAccZ = property(_sarakitdevices.InfoAccGyro_rawAccZ_get, _sarakitdevices.InfoAccGyro_rawAccZ_set)
    rawGyroX = property(_sarakitdevices.InfoAccGyro_rawGyroX_get, _sarakitdevices.InfoAccGyro_rawGyroX_set)
    rawGyroY = property(_sarakitdevices.InfoAccGyro_rawGyroY_get, _sarakitdevices.InfoAccGyro_rawGyroY_set)
    rawGyroZ = property(_sarakitdevices.InfoAccGyro_rawGyroZ_get, _sarakitdevices.InfoAccGyro_rawGyroZ_set)

    def __init__(self):
        _sarakitdevices.InfoAccGyro_swiginit(self, _sarakitdevices.new_InfoAccGyro())
    __swig_destroy__ = _sarakitdevices.delete_InfoAccGyro

# Register InfoAccGyro in _sarakitdevices:
_sarakitdevices.InfoAccGyro_swigregister(InfoAccGyro)

class InfoEncoders(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    angle = property(_sarakitdevices.InfoEncoders_angle_get, _sarakitdevices.InfoEncoders_angle_set)
    velocity = property(_sarakitdevices.InfoEncoders_velocity_get, _sarakitdevices.InfoEncoders_velocity_set)
    angleDeg = property(_sarakitdevices.InfoEncoders_angleDeg_get, _sarakitdevices.InfoEncoders_angleDeg_set)
    velocityDeg = property(_sarakitdevices.InfoEncoders_velocityDeg_get, _sarakitdevices.InfoEncoders_velocityDeg_set)
    direction = property(_sarakitdevices.InfoEncoders_direction_get, _sarakitdevices.InfoEncoders_direction_set)
    zeroAngle = property(_sarakitdevices.InfoEncoders_zeroAngle_get, _sarakitdevices.InfoEncoders_zeroAngle_set)

    def __init__(self):
        _sarakitdevices.InfoEncoders_swiginit(self, _sarakitdevices.new_InfoEncoders())
    __swig_destroy__ = _sarakitdevices.delete_InfoEncoders

# Register InfoEncoders in _sarakitdevices:
_sarakitdevices.InfoEncoders_swigregister(InfoEncoders)

class initFOC(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ready = property(_sarakitdevices.initFOC_ready_get, _sarakitdevices.initFOC_ready_set)
    angleZero = property(_sarakitdevices.initFOC_angleZero_get, _sarakitdevices.initFOC_angleZero_set)
    direction = property(_sarakitdevices.initFOC_direction_get, _sarakitdevices.initFOC_direction_set)

    def __init__(self):
        _sarakitdevices.initFOC_swiginit(self, _sarakitdevices.new_initFOC())
    __swig_destroy__ = _sarakitdevices.delete_initFOC

# Register initFOC in _sarakitdevices:
_sarakitdevices.initFOC_swigregister(initFOC)

class GetInfoResult(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    idata1 = property(_sarakitdevices.GetInfoResult_idata1_get, _sarakitdevices.GetInfoResult_idata1_set)
    idata2 = property(_sarakitdevices.GetInfoResult_idata2_get, _sarakitdevices.GetInfoResult_idata2_set)
    idata3 = property(_sarakitdevices.GetInfoResult_idata3_get, _sarakitdevices.GetInfoResult_idata3_set)
    fdata1 = property(_sarakitdevices.GetInfoResult_fdata1_get, _sarakitdevices.GetInfoResult_fdata1_set)
    fdata2 = property(_sarakitdevices.GetInfoResult_fdata2_get, _sarakitdevices.GetInfoResult_fdata2_set)
    fdata3 = property(_sarakitdevices.GetInfoResult_fdata3_get, _sarakitdevices.GetInfoResult_fdata3_set)
    bdata1 = property(_sarakitdevices.GetInfoResult_bdata1_get, _sarakitdevices.GetInfoResult_bdata1_set)
    bdata2 = property(_sarakitdevices.GetInfoResult_bdata2_get, _sarakitdevices.GetInfoResult_bdata2_set)
    bdata3 = property(_sarakitdevices.GetInfoResult_bdata3_get, _sarakitdevices.GetInfoResult_bdata3_set)

    def __init__(self):
        _sarakitdevices.GetInfoResult_swiginit(self, _sarakitdevices.new_GetInfoResult())
    __swig_destroy__ = _sarakitdevices.delete_GetInfoResult

# Register GetInfoResult in _sarakitdevices:
_sarakitdevices.GetInfoResult_swigregister(GetInfoResult)

_PI = _sarakitdevices._PI
_2PI = _sarakitdevices._2PI
DEG_TO_RAD = _sarakitdevices.DEG_TO_RAD
RAD_TO_DEG = _sarakitdevices.RAD_TO_DEG

def sleepms(ms):
    return _sarakitdevices.sleepms(ms)

def sendCommandSet(buffer):
    return _sarakitdevices.sendCommandSet(buffer)

def sendCommandGet(buffer, len):
    return _sarakitdevices.sendCommandGet(buffer, len)

def _SPICheck():
    return _sarakitdevices._SPICheck()

def BLDCMotor_Reset():
    return _sarakitdevices.BLDCMotor_Reset()

def Sensors_On(enable):
    return _sarakitdevices.Sensors_On(enable)

def getAccGyro():
    return _sarakitdevices.getAccGyro()

def getTemperature():
    return _sarakitdevices.getTemperature()

def LSM6DS3TR_readRegisters(address, data, length):
    return _sarakitdevices.LSM6DS3TR_readRegisters(address, data, length)

def LSM6DS3TR_writeRegisters(address, data):
    return _sarakitdevices.LSM6DS3TR_writeRegisters(address, data)

def GyroCalib():
    return _sarakitdevices.GyroCalib()

def AccCalib():
    return _sarakitdevices.AccCalib()

def Encoder_On(EncoderId, enable):
    return _sarakitdevices.Encoder_On(EncoderId, enable)

def Encoder_Param(EncoderId, minpwm, maxpwm):
    return _sarakitdevices.Encoder_Param(EncoderId, minpwm, maxpwm)

def Encoder_LowPassFilter(EncoderId, angle, velocity):
    return _sarakitdevices.Encoder_LowPassFilter(EncoderId, angle, velocity)

def Encoder_Get(EncoderId):
    return _sarakitdevices.Encoder_Get(EncoderId)

def Encoder_GetParam(EncoderId):
    return _sarakitdevices.Encoder_GetParam(EncoderId)

def BLDCMotor_PolePairs(motorId, polePairs):
    return _sarakitdevices.BLDCMotor_PolePairs(motorId, polePairs)

def BLDCMotor_On(motorId, enable):
    return _sarakitdevices.BLDCMotor_On(motorId, enable)

def BLDCMotor_IdleTorque(motorId, torque, torqueMs):
    return _sarakitdevices.BLDCMotor_IdleTorque(motorId, torque, torqueMs)

def BLDCMotor_PIDAngle(motorId, P, I, D, ramp):
    return _sarakitdevices.BLDCMotor_PIDAngle(motorId, P, I, D, ramp)

def BLDCMotor_PIDVelocity(motorId, P, I, D, ramp):
    return _sarakitdevices.BLDCMotor_PIDVelocity(motorId, P, I, D, ramp)

def BLDCMotor_InitFOC(motorId, encoderId, direction, angle):
    return _sarakitdevices.BLDCMotor_InitFOC(motorId, encoderId, direction, angle)

def BLDCMotor_MoveToAngle(motorId, angle, speed, torque, degrees):
    return _sarakitdevices.BLDCMotor_MoveToAngle(motorId, angle, speed, torque, degrees)

def BLDCMotor_MoveByAngle(motorId, angle, speed, torque, degrees):
    return _sarakitdevices.BLDCMotor_MoveByAngle(motorId, angle, speed, torque, degrees)

def BLDCMotor_DriveMeters(motorId, centimeters, speed, torque, WhellDiameter):
    return _sarakitdevices.BLDCMotor_DriveMeters(motorId, centimeters, speed, torque, WhellDiameter)

def BLDCMotor_MoveContinuousTorque(motorId, direction, torque):
    return _sarakitdevices.BLDCMotor_MoveContinuousTorque(motorId, direction, torque)

def BLDCMotor_MoveContinuousVelocity(motorId, direction, torque, speed, degrees):
    return _sarakitdevices.BLDCMotor_MoveContinuousVelocity(motorId, direction, torque, speed, degrees)

def BLDCMotor_MoveStop(motorId):
    return _sarakitdevices.BLDCMotor_MoveStop(motorId)

def BLDCMotor_GetInfo(motorId, info, zprint):
    return _sarakitdevices.BLDCMotor_GetInfo(motorId, info, zprint)

