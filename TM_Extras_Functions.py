import bpy
import mathutils
import math
from . utility_function import *

def create_Light(name="Light", type="SUN", energy=30):
    light_data = bpy.data.lights.new(name=name, type=type)
    light_data.energy = energy
    light_object = bpy.data.objects.new(name=name, object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    
    return light_object


def create_Camera(name="Camera"):
    camera_data = bpy.data.cameras.new(name=name)
    camera_object = bpy.data.objects.new(name=name, object_data=camera_data)
    bpy.context.collection.objects.link(camera_object)
    
    return camera_object


def object_offset(object, offsetX = 0, offsetY = 0, offsetZ = 0):
    

    
    vec = mathutils.Vector((offsetX*object.scale[0], offsetY*object.scale[1], offsetZ*object.scale[2]))
    

    
    inv = object.matrix_world.copy()
    inv.invert()
    
    vec_rot = vec @ inv
    offset = object.location + vec_rot
    
    print(offset)
    
    return offset



def create_Light_object_offset(object, name="Light", type="SUN", energy=30, offsetX = 5.0, offsetY = 0, offsetZ = 0):

    offset = object_offset(object,offsetX,offsetY,offsetZ)
    

    light = create_Light(name, type, energy)
    light.location = offset
    
    return light



def Create_3PL(object):
    
    dimX = object.dimensions.x
    dimY = object.dimensions.y
    dimZ = object.dimensions.z
    
    scale_X = object.scale.x
    scale_Y = object.scale.y
    scale_Z = object.scale.z
    
    Mainlight = create_Light_object_offset(object, name="Main_Light", type="SUN", energy=2, offsetX = dimX/scale_X, offsetY = -dimY/scale_Y, offsetZ = dimZ/scale_Z)
    Fillight = create_Light_object_offset(object, name="Fill_Light", type="SUN", energy=1, offsetX = -dimX/scale_X, offsetY = -dimY/scale_Y, offsetZ = dimZ/scale_Z)
    Rimlight = create_Light_object_offset(object, name="Rim_Light", type="SUN", energy=5, offsetX = dimX/scale_X, offsetY = dimY/scale_Y, offsetZ = dimZ/scale_Z)
    
    print(dimX)
    print(dimY)
    print(dimZ)
    
    # Mainlight.parent = object
    # Fillight.parent = object
    # Rimlight.parent = object
    
    
    constraint = Mainlight.constraints.new("TRACK_TO")
    constraint.target = object
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    

    
    constraint = Fillight.constraints.new("TRACK_TO")
    constraint.target = object
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    

    
    constraint = Rimlight.constraints.new("TRACK_TO")
    constraint.target = object
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    

def create_Camera_Fit(object, offset = 0):
    
    

            
    cam = create_Camera()
#    cam.parent = object
    
    if object.vertex_groups.get("All"):
        pass
    else:
        vg = object.vertex_groups.new(name="All")
        verts=[]
        
        for vert in object.data.vertices:
            verts.append(vert.index)
        vg.add(verts, 1.0, "ADD")
    
    

    constraint = cam.constraints.new("TRACK_TO")
    constraint.target = object
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    try:
        constraint.subtarget = vg.name
    except:
        pass
    
    compare_dimension = max([object.dimensions.x, object.dimensions.y, object.dimensions.z]) * 3 + offset

    

    
    offset = object_offset(object, offsetY=-compare_dimension)
    cam.location = offset
    cam.data.clip_end = 100000


    bpy.context.scene.camera = cam

    region = next(iter([area.spaces[0].region_3d for area in bpy.context.screen.areas if area.type == 'VIEW_3D']), None)
    if region:
        region.view_perspective = 'CAMERA'



def create_Turnaround_Camera(self, context, direction=1, frame_Range=1, axis=2, isHideEmpty=False, custom_range=100, repeat=1, offset = 0):
    
    
    cam = create_Camera()
    
    object = context.object

    scn = context.scene

    if object:
        input = object.location
        rotatempty = create_empty("AimTarget", input)

        cam.parent = rotatempty
        rotatempty.parent = object
    else:

        input = (0, 0, 0)

        rotatempty = create_empty("AimTarget", input)
        cam.parent = rotatempty

    
    constraint = cam.constraints.new("TRACK_TO")
    constraint.target = rotatempty
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    try:
        constraint.subtarget = vg.name
    except:
        pass
    
    if object:
        compare_dimension = max([object.dimensions.x, object.dimensions.y, object.dimensions.z]) * 3 + offset
    else:
        compare_dimension = max([10, 10, 10]) + offset

    

    if object:
        offset = object_offset(object, offsetY=-compare_dimension, offsetZ=compare_dimension)
    else:
        offset = object_offset(rotatempty, offsetY=-compare_dimension, offsetZ=compare_dimension)

    cam.location = offset
    cam.data.clip_end = 100000


    bpy.context.scene.camera = cam

    # region = next(iter([area.spaces[0].region_3d for area in bpy.context.screen.areas if area.type == 'VIEW_3D']), None)
    # if region:
    #     region.view_perspective = 'CAMERA'

    object  = rotatempty



    #Preparing the Expression for driver
    
    if bool(int(direction)):


        expr_direction = ""
    else:

        expr_direction = "-"


    expr_repeat = str(repeat)

    if bool(int(frame_Range)):
        expr_frame_range = "end-start"
    else:
        expr_frame_range = str(custom_range)

    Expression = "%sradians(radians((frame-start)*%s)*359/radians(%s))" % (expr_direction, expr_repeat, expr_frame_range)

    #Empty Creation

    Empty_Location = object.location


    New_Turnaround_Empty = object


    #Driver Creation
    #Create Driver Variable

    Empty_Driver = New_Turnaround_Empty.driver_add("rotation_euler", int(axis))

    start = Empty_Driver.driver.variables.new()
    start.name = "start"
    start.targets[0].id_type = "SCENE"
    start.targets[0].id = scn
    start.targets[0].data_path = "frame_end"   

    end = Empty_Driver.driver.variables.new()
    end. name = "end"
    end.targets[0].id_type = "SCENE"
    end.targets[0].id = scn
    end.targets[0].data_path = "frame_start"
    
    Empty_Driver.driver.expression = Expression

    return New_Turnaround_Empty






























def create_Aim_Camera(object, offset = 0, targetEmpty=True):
    
    
    cam = create_Camera()

    if targetEmpty:
        input = (0, 0, 0)
        object = create_empty("AimTarget", input)

    #    cam.parent = object

    
    

    constraint = cam.constraints.new("TRACK_TO")
    constraint.target = object
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    try:
        constraint.subtarget = vg.name
    except:
        pass
    
    compare_dimension = max([object.dimensions.x, object.dimensions.y, object.dimensions.z]) * 3 + offset

    

    
    offset = object_offset(object, offsetY=-compare_dimension, offsetZ=compare_dimension)
    cam.location = offset
    cam.data.clip_end = 100000


    bpy.context.scene.camera = cam



