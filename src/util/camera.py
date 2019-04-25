from util.ray import ray
from util.vector import vec3

class viewport :
    def __init__(self, left_bottom, width, height) :
        self.left_bottom  = left_bottom
        self.width        = width
        self.height       = height

    def get_inner_point(self, u, v):
        return self.left_bottom + vec3(self.width * u, 0.0, 0.0) + vec3(0.0, self.height * v, 0.0)

class camera :
    def __init__(self, position, vp) :
        self.position = position
        self.vp = vp

    def get_ray(self, u, v) :
        direction = self.vp.get_inner_point(u, v) - self.position
        return ray(self.position, vec3.normalize(direction))