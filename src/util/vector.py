from math import sqrt
from random import random

class vec3 :
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def length(v) :
        return sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2)

    @staticmethod
    def normalize(v) :
        v_len = vec3.length(v)
        if v_len == 0 :
            raise ZeroDivisionError        
        unit_v = vec3(v.x, v.y, v.z) / v_len
        return unit_v

    @staticmethod
    def interpolate(v1, v2, t) :
        return v1 * t + v2 * (1.0 - t)

    @staticmethod
    def dot(v1, v2) :
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def reflect(v, n) :
        return v - 2 * vec3.dot(v, n) * n

    @staticmethod
    def get_random_in_sphere() :
        while True:
            v = vec3(random(), random(), random()) * 2.0 - 1.0
            if vec3.length(v) < 1.0 :
                return v

    def __add__(self, other) :
        if isinstance(other, self.__class__) :
            return vec3( self.x + other.x, self.y + other.y, self.z + other.z )
        else :
            return vec3( self.x + other,   self.y + other,   self.z + other   )
    
    def __sub__(self, other) :
        if isinstance(other, self.__class__) :
            return vec3( self.x - other.x, self.y - other.y, self.z - other.z )
        else :
            return vec3( self.x - other,   self.y - other,   self.z - other   )
    def __mul__(self, other) :
        if isinstance(other, self.__class__) :
            return vec3( self.x * other.x, self.y * other.y, self.z * other.z )
        else :
            return vec3( self.x * other,   self.y * other,   self.z * other   )
    def __truediv__(self, other) :
        if isinstance(other, self.__class__) :
            return vec3( self.x / other.x, self.y / other.y, self.z / other.z )
        else :
            return vec3( self.x / other,   self.y / other,   self.z / other   )
        
    __radd__     = __add__
    __rsub__     = __sub__
    __rmul__     = __mul__
# end of vector class