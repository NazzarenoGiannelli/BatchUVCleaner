bl_info = {
'name': 'UVCleaner',
'author': 'Nazzareno Giannelli',
'version': (1, 0),
'blender': (2, 83, 0),
'location': 'View3D > Object > UVCleaner',
'description': 'Leaves only the active render UV channel to every mesh in the scene',
'wiki_url': '',
'tracker_url': '',
'category': '3D View'}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

class OBJECT_OT_uvcleaner(Operator):
    bl_label = 'UVCleaner'
    bl_idname = 'object.uvcleaner'
    bl_description = 'Leaves only the active render UV channel to every mesh in the scene'
    bl_space_type = 'VIEW_3D'
    bl_region_type= 'UI'
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        for x in bpy.data.meshes:
            uvs = [uv for uv in x.uv_layers
                    if not uv.active_render]
            while uvs:
                x.uv_layers.remove(uvs.pop())
                               
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_uvcleaner.bl_idname)
    
def register():
    bpy.utils.register_class(OBJECT_OT_uvcleaner)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_uvcleaner)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
if __name__ == '__main__':
    register()