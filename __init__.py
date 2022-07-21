
bl_info = {
    "name": "Make Turnaround",
    "author": "BlenderBoi",
    "version": (1, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Make Turnaround",
    "description": "Creates Turnaround",
    "warning": "This Addon is No Longer Being Maintained by BlenderBoi, Feel free to Fork this Addon and Maintain it. ",
    "wiki_url": "",
    "category": "Object",
}

import bpy
from . import TM_Operators
from .  import TM_Extras_Operators

def register():

    TM_Operators.register()
    TM_Extras_Operators.register()

def unregister():

    TM_Operators.unregister()
    TM_Extras_Operators.unregister()


if __name__ == "__main__":
    register()
