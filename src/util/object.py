from abc import ABC
from util.vector import vec3
from util.material import material, lambertian
from math import sqrt

# store information about hit event
class hit_record :
    def __init__(self) :
        self.bHit     = False
        self.point    = vec3(0.0, 0.0, 0.0)
        self.normal   = vec3(0.0, 0.0, 0.0)
        self.material = material()
        self.t        = 100000000.0

# hitable interface 
class hitable(ABC) :
    def hit(self, r, t_min, t_max, h_record) :
        raise NotImplementedError("Subclass must implement hit method")

class sphere(hitable) :
    def __init__(self, position, radius, mesh_material=lambertian(vec3(0.5, 0.5, 0.5))) :
        self.position      = position
        self.radius        = radius
        self.mesh_material = mesh_material
    
    def hit(self, r, t_min, t_max, h_record) :
        """
        param1 : input ray
        param2 : min value of t (for represent vector in form A + B * t)
        param3 : max value of t (for represent vector in form A + B * t)
        param4 : previous hit record
        """
        oc  = r.get_origin() - self.position
        dir = r.get_direction()

        a = vec3.dot(dir, dir)
        b = vec3.dot(oc, dir)
        c = vec3.dot(oc, oc) - self.radius ** 2
        D = b ** 2 - a * c

        if D > 0.0 :
            temp = ( -b - sqrt( D ) ) / a
            if temp > t_min and temp < t_max :
                h_record.t = temp
                h_record.point    = r.get_point_at(temp)
                h_record.normal   = vec3.normalize(h_record.point - self.position)
                h_record.bHit     = True
                h_record.material = self.mesh_material
                return h_record
            
            temp = ( -b + sqrt( D ) ) / a
            if temp > t_min and temp < t_max :
                h_record.t = temp
                h_record.point    = r.get_point_at(temp)
                h_record.normal   = vec3.normalize(h_record.point - self.position)
                h_record.bHit     = True
                h_record.material = self.mesh_material
                return h_record
        
        h_record.bHit = False
        return h_record
        
        