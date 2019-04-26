from util.ray    import ray
from util.vector import vec3
from util.object import hit_record, sphere
from util.util   import split_file_name
from util.camera import viewport, camera
import sys
from random import random

def shoot_ray(r, obj_list) :
    record = hit_record()
    for obj in obj_list:
        record = obj.hit(r, 0, record.t, record)
        if record.bHit == True : break
    
    # if given ray hit some object, get normal vector from hit record.
    # Finally, saturates each elements of normal vector to range 0 ~ 1
    if record.bHit == True :
        return (record.normal + 1.0) * 0.5
    
    dir = r.get_direction()
    t = (dir.y + 1.0) * 0.5
    return vec3.interpolate(vec3(0.5, 0.7, 1.0), vec3(1.0, 1.0, 1.0), t)

if __name__ == "__main_ _" :
    width  = 200
    height = 100
    # large num_samples : improved aliasing artifact. very slow.
    # small num_samples : less improved aliasing artifact. fast ever than before.
    num_samples = 60
    name   = split_file_name(abs_path=sys.argv[0]) + ".ppm"

    cam = camera(vec3(0.0, 0.0, 0.0), viewport( vec3(-2.0, -1.0, -1.0), 4.0, 2.0))
    obj_list = [
        sphere(vec3(0.0, 0.0, -1.0), 0.5),
        sphere(vec3(0.0, -100.5, -1.0), 100.0)
    ]

    with open(name, 'w') as f :
        f.write("P3\n{0:d} {1:d}\n255\n".format(width, height)) # write ppm file header
        for j in range(height - 1, -1, -1) : # j begin from height - 1, end at 0
            for i in range(0, width, 1) :          # i begin from 0, end at width - 1

                # Anti-Aliasing process.
                total_color = vec3(0.0, 0.0, 0.0)
                for s in range(num_samples) :
                    # randomly get points u, v which are in range i ~ i + 1, j ~ j + 1
                    u = (i + random()) / float(width )
                    v = (j + random()) / float(height)
                    r = cam.get_ray(u, v)
                    # add ray-tracing result color to total-color variable.
                    total_color = total_color + shoot_ray(r, obj_list)
                # divide total_color with num_samples for averaging.
                color = total_color / float(num_samples)

                ir = int( color.x * 255 )
                ig = int( color.y * 255 )
                ib = int( color.z * 255 )
    
                f.write("{0:d} {1:d} {2:d}\n".format(ir, ig, ib))