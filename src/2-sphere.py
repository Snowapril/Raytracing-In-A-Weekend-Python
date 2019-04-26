from util.ray    import ray
from util.vector import vec3
from util.object import hit_record, sphere
from util.util   import split_file_name
from util.camera import viewport, camera
import sys

def shoot_ray(r, obj_list) :
    """
    detail : shoot ray from camera to target grid hole.
    param1 : ray class instance which have origin point and direction vector
    param2 : object list that will be rendered.
    """
    record = hit_record()
    # find object which collided by given ray through "for loop".
    for obj in obj_list:
        record = obj.hit(r, 0.00001, record.t, record)
    
    # if given ray hit the object, return green color (r = 0, g = 1, b = 0),
    # otherwise, return background color.
    if record.bHit == True :
        return vec3(0.0, 1.0, 0.0)
    else:
        dir = r.get_direction()
        t = (dir.y + 1.0) * 0.5
        return vec3.interpolate(vec3(0.5, 0.7, 1.0), vec3(1.0, 1.0, 1.0), t)

if __name__ == "__main__" :
    width  = 200
    height = 100
    name   = split_file_name(abs_path=sys.argv[0]) + ".ppm"

    # set camera on origin point and place viewport rectangle .
    cam = camera(vec3(0.0, 0.0, 0.0), viewport( vec3(-2.0, -1.0, -1.0), 4.0, 2.0))
    obj_list = [
        sphere(vec3(0.0, 0.0, -1.0), 0.5)
    ]

    with open(name, 'w') as f :
        f.write("P3\n{0:d} {1:d}\n255\n".format(width, height)) # write ppm file header
        for j in range(height - 1, -1, -1) : # j begin from height - 1, end at 0
            for i in range(0, width, 1) :          # i begin from 0, end at width - 1
                u = i / float(width )
                v = j / float(height)
    
                # u and v will be in range 0 ~ 1.
                # get ray from given u, v coordinates
                r = cam.get_ray(u, v)
                color = shoot_ray(r, obj_list)
                    
                ir = int( color.x * 255 )
                ig = int( color.y * 255 )
                ib = int( color.z * 255 )
    
                f.write("{0:d} {1:d} {2:d}\n".format(ir, ig, ib))