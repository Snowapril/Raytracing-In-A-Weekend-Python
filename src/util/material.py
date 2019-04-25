from abc import ABC
from util.ray import ray
from util.vector import vec3

class material_record :
    def __init__(self) :
        self.bScattered = False
        self.scattered_ray = ray(vec3(0.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0))
        self.attenuation = vec3(0.0, 0.0, 0.0)

# material interface 
class material(ABC) :
    def scatter(self, r, h_record) :
        """
        param1 : input ray
        param2 : hit record (hit point, normal, etc ...)
        param3 : material record (scatter result, ray, attenuation, etc ...)
        """
        raise NotImplementedError("Subclass must implement scatter method")

class lambertian(material) :
    def __init__(self, albedo) :
        self.albedo = albedo 

    def scatter(self, r, h_record) :
        target = h_record.point + h_record.normal + vec3.get_random_in_sphere()

        m_record = material_record()
        m_record.scattered_ray = ray(h_record.point, target - h_record.point)
        m_record.attenuation = self.albedo
        m_record.bScattered = True

        return m_record

class metal(material) :
    def __init__(self, albedo, fuzz) :
        self.albedo = albedo
        self.fuzz   = min(fuzz, 1.0)

    def scatter(self, r, h_record) :
        reflected = vec3.reflect(vec3.normalize(r.get_direction()), h_record.normal)
        direction = reflected + self.fuzz * vec3.get_random_in_sphere()

        m_record = material_record()
        m_record.scattered_ray = ray(h_record.point, direction)
        m_record.attenuation = self.albedo
        m_record.bScattered = vec3.dot( m_record.scattered_ray.get_direction(), h_record.normal ) > 0

        return m_record