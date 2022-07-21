import bpy
from . TM_Functions import *


class TM_OT_Make_Tunraround(bpy.types.Operator):
    """Creates a Turnaround from selected object"""
    bl_idname = "tm.make_turnaround"
    bl_label = "Make Turnaround"

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

    pivot: bpy.props.EnumProperty(
        name="Pivot",
        items=(("ORIGIN", "Origin", "Use Object Origin"), ("CENTER", "Center", "Use Object Center"),  ("BOTTOM_VERTEX", "Bottom Vertex", "Average of Vertices with the lowest Z-Value"), ("BOTTOM_CENTER", "Bottom Center", "Center of the object with the lowest Z-Value")),
        default = "BOTTOM_CENTER"
        )

    repeat: bpy.props.IntProperty(name ="Repeat", default=1, min=0)

    isHideEmpty: bpy.props.BoolProperty(name="Hide Empty", default = False)

    custom_range : bpy.props.IntProperty(name = "Custom Range", default = 100)




    def execute(self, context):
        
        object = context.active_object
        
        if object:
            
            
            Empty = Create_Turnaround(self, context, direction=self.direction, frame_Range=self.frame_range, axis=self.axis, pivot=self.pivot, isHideEmpty=self.isHideEmpty, custom_range=self.custom_range, repeat=self.repeat)
            if self.isHideEmpty:
                Empty.hide_set(True)


        else:
            self.report({"ERROR"}, "No active object")
            
        return {'FINISHED'}

            
    def draw(self, context):

        layout = self.layout

        layout.prop(self,"direction")
        layout.prop(self,"axis")
        layout.prop(self,"pivot")
        layout.prop(self,"isHideEmpty")

        layout.prop(self,"frame_range")
        if self.frame_range == "0":
            layout.prop(self,"custom_range")
        layout.prop(self,"repeat", text="Rotation / Cycle")

    def invoke(self, context, event):
        
        if context.active_object:
            return context.window_manager.invoke_props_dialog(self)
        else:
            self.report({"ERROR"}, "No Active Object")
            return{'CANCELLED'}







def tm_make_turnaround_menu_draw(self, context):
    self.layout.operator("tm.make_turnaround", text="Make Turnaround")



classes=[TM_OT_Make_Tunraround]

def register():
    
    for c in classes:
        bpy.utils.register_class(c)
    
    # bpy.types.VIEW3D_MT_object.append(tm_make_turnaround_menu_draw)

    # bpy.types.VIEW3D_MT.append(tm_make_turnaround_menu_draw)
    

    
def unregister():

    for c in classes:
        bpy.utils.unregister_class(c)
        
    # bpy.types.VIEW3D_MT_object.remove(tm_make_turnaround_menu_draw)

    # bpy.types.VIEW3D_MT.remove(tm_make_turnaround_menu_draw)
    

    
if __name__ == '__main__':
    register()