import bpy
from . utility_function import *


def Create_Turnaround(self, context, direction=1, frame_Range=1, axis=2, pivot="BOTTOM_CENTER", isHideEmpty=False, custom_range=100, repeat=1):



    obj = context.object
    obj_name = obj.name
    obj_location = obj.location

    scn = context.scene

    


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

    Empty_Name = "%s_Turnaround_Empty" % (obj_name)

    if obj.type == "MESH":
        if pivot == "BOTTOM_CENTER":
            Empty_Location = find_lowest_point(obj, center=True)
        elif pivot == "ORIGIN":
            Empty_Location = obj_location
        elif pivot == "CENTER":
            Empty_Location = find_center_point(obj)
        elif pivot == "BOTTOM_VERTEX":
            Empty_Location = find_lowest_point(obj, center=False)
    else:

        Empty_Location = obj_location


    New_Turnaround_Empty = create_empty(Empty_Name, Empty_Location)




    #Add Parent Constraint
    constraint = obj.constraints.new('CHILD_OF')
    constraint.target = New_Turnaround_Empty
    constraint.set_inverse_pending = True


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