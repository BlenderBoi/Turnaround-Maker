import bpy
import numpy as np

def find_center_point(obj):
    
    pts = [(obj.matrix_world @ v.co) for v in obj.data.vertices]
    center_pt = np.average(pts, 0)
    
    return center_pt
    

def find_lowest_point(obj, center=False):
    
    lowest_pt = min([(obj.matrix_world @ v.co).z for v in obj.data.vertices])
    lowest_z = min([(obj.matrix_world @ v.co).z for v in obj.data.vertices])
    lowest_pts = [(obj.matrix_world @ v.co) for v in obj.data.vertices if (obj.matrix_world @ v.co).z == lowest_z]
    lowest_pt = np.average(lowest_pts, 0)
    
    if center == True:
        lowest_pt_center = find_center_point(obj)
        lowest_pt_center[2] = lowest_pt[2]
        return lowest_pt_center
    
    else:
        return lowest_pt
        
    
def create_empty(name, input):

    o = bpy.data.objects.new( name, None )
    bpy.context.scene.collection.objects.link( o )
    o.empty_display_size = 2
    o.empty_display_type = 'PLAIN_AXES'  
    
    try:
        o.matrix_world = input.matrix_world
        return o
    except:
        try:
            o.matrix_world = input
            return o 
        except:
            try:
                o.location = input
                return o
            except:
                print("Wrong Type")
        
        