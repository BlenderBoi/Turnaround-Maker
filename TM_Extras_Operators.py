import bpy
from . TM_Extras_Functions import *
from . TM_Operators import *

class TM_OT_Add_Fit_Camera(bpy.types.Operator):
    """Creates a Camera that fit the selected object into view"""
    bl_idname = "tm.extras_fit_camera"
    bl_label = "Fit Camera"


    def execute(self, context):
        
        object = context.active_object
        
        if object:

            create_Camera_Fit(object, offset=10)

        else:
            self.report({"ERROR"}, "No active object")
            
        return {'FINISHED'}





class TM_OT_Add_Turnaround_Camera(bpy.types.Operator):
    """Creates a Camera that Rotates around a Object"""
    bl_idname = "tm.extras_turnaround_camera"
    bl_label = "Turnaround Camera"

    direction: bpy.props.EnumProperty(
        name="Direction",
        items=(("1", "Left", "Make Turnaround turn left"), ("0", "Right", "Make Turnaround turn right")),
        default = "1"
        )

    frame_range : bpy.props.EnumProperty(
        name="Length",
        items=(("1", "Frame Range", "Use Frame Range"), ("0", "Custom Length", "Use Custom Length")),
        default = "1"
    )

    axis: bpy.props.EnumProperty(
        name="Axis",
        items=(("0", "X", "X-Axis"), ("1", "Y", "Y-Axis"),  ("2", "Z", "Z-Axis")),
        default = "2"
        )


    repeat: bpy.props.IntProperty(name ="Repeat", default=1, min=0)

    # isHideEmpty: bpy.props.BoolProperty(name="Hide Empty", default = False)

    custom_range : bpy.props.IntProperty(name = "Custom Range", default = 100)




    def execute(self, context):
        
        object = context.active_object
        

        Empty = create_Turnaround_Camera(self, context, direction=self.direction, frame_Range=self.frame_range, axis=self.axis, custom_range=self.custom_range, repeat=self.repeat)


            
        return {'FINISHED'}

            
    def draw(self, context):

        layout = self.layout

        layout.prop(self,"direction")
        layout.prop(self,"axis")
        layout.prop(self,"isHideEmpty")

        layout.prop(self,"frame_range")
        if self.frame_range == "0":
            layout.prop(self,"custom_range")
        layout.prop(self,"repeat", text="Rotation / Cycle")

    def invoke(self, context, event):
        

        return context.window_manager.invoke_props_dialog(self)




































class TM_OT_Add_Aim_Camera(bpy.types.Operator):
    """Creates a Camera that aims at a Object"""
    bl_idname = "tm.extras_aim_camera"
    bl_label = "Aim Camera"


    def execute(self, context):
        
        object = context.active_object
        
        if object:

            create_Aim_Camera(object, offset=10, targetEmpty=False)
        else:
            create_Aim_Camera(object, offset=10, targetEmpty=True)
            
        return {'FINISHED'}



class TM_OT_Add_Three_Point_Light(bpy.types.Operator):
    """Creates a 3 point light on object"""
    bl_idname = "tm.extras_three_point_light"
    bl_label = "Three Point Light"


    def execute(self, context):
        
        object = context.active_object
        
        if object:

            Create_3PL(object)

        else:
            self.report({"ERROR"}, "No active object")
            
        return {'FINISHED'}

            

class Turnaround_Maker_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_camera_turnaroundmaker"
    bl_label = "Turnaround Maker"

    def draw(self, context):

        layout = self.layout

        self.layout.operator("tm.make_turnaround", icon='CURSOR')
        self.layout.operator("tm.extras_fit_camera", icon='VIEW_CAMERA')
        self.layout.operator("tm.extras_turnaround_camera", icon='VIEW_CAMERA')
        self.layout.operator("tm.extras_aim_camera", icon='VIEW_CAMERA')
        self.layout.operator("tm.extras_three_point_light", icon='OUTLINER_OB_LIGHT')



def TM_add_Camera_Menu(self, context):
    self.layout.operator("tm.extras_fit_camera", icon='VIEW_CAMERA')
    self.layout.operator("tm.extras_turnaround_camera", icon='VIEW_CAMERA')
    self.layout.operator("tm.extras_aim_camera", icon='VIEW_CAMERA')


def TM_add_Light_Menu(self, context):
    self.layout.operator("tm.extras_three_point_light", icon='OUTLINER_OB_LIGHT')


def TM_Turnaround_Maker_Menu(self, context):
    
    self.layout.menu("VIEW3D_MT_camera_turnaroundmaker", icon='CURSOR')

classes=[
        TM_OT_Add_Fit_Camera,
        TM_OT_Add_Three_Point_Light,
        TM_OT_Add_Turnaround_Camera,
        TM_OT_Add_Aim_Camera,

        Turnaround_Maker_Menu
        ]

def register():
    
    for c in classes:
        bpy.utils.register_class(c)
    
    # bpy.types.VIEW3D_MT_camera_add.append(TM_add_Camera_Menu)
    # bpy.types.VIEW3D_MT_light_add.append(TM_add_Light_Menu)

    bpy.types.VIEW3D_MT_add.append(TM_Turnaround_Maker_Menu)




    
def unregister():

    for c in classes:
        bpy.utils.unregister_class(c)
        
    # bpy.types.VIEW3D_MT_camera_add.remove(TM_add_Camera_Menu)
    # bpy.types.VIEW3D_MT_light_add.remove(TM_add_Light_Menu)

    bpy.types.VIEW3D_MT_add.remove(TM_Turnaround_Maker_Menu)
    

    
if __name__ == '__main__':
    register()