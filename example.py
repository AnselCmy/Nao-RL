import ctypes
import math


# declare the return type of Kinematics
class Pos(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float)
    ]

# load c++ library as lib
lib = ctypes.cdll.LoadLibrary('./release/base.so')

# init the joint angles of nao
num_angles = 24
angles = (ctypes.c_float*num_angles)()
for i in range(num_angles):
    angles[i] = 0

# declare the angles of right arm
arm0 = 18
angles[arm0 + 0] = math.pi
angles[arm0 + 1] = 0
angles[arm0 + 2] = 0
angles[arm0 + 3] = -math.pi / 2

lib.Kinematics.restype = Pos
pos = lib.Kinematics(angles)
print(pos.x, pos.y, pos.z)
