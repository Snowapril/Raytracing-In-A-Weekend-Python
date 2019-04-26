import sys
from util.util import split_file_name

if __name__ == "__main__" :
    # set image size
    width  = 200
    height = 100
    # set image name with current executed python file name.
    name   = split_file_name(sys.argv[0]) + ".ppm"

    with open(name, 'w') as f :
        # write ppm file header
        f.write("P3\n{0:d} {1:d}\n255\n".format(width, height)) 
        
        # traverse whole width * height pixels with two for loops.
        for j in range(height - 1, -1, -1) : # j begin from height - 1, end at 0
            for i in range(width) :          # i begin from 0, end at width - 1
                r = i / float(width )        
                g = j / float(height)       
                b = 0.2

                ir = int( r * 255 )
                ig = int( g * 255 )
                ib = int( b * 255 )

                # write R G B three integers on ppm file.
                f.write("{0:d} {1:d} {2:d}\n".format(ir, ig, ib))
    #end of file i/o