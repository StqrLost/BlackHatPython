from ctypes import *
import socket
import struct

class IP(Structure):
    _fields_ =[
        ("version",     c_ubyte,    4),
        ("ihl",     c_ubyte,    4)
    ]