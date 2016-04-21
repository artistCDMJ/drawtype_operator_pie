import bpy
from bpy.types import Menu

#operators

#wire draw
class WireFrame(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.wire_frame"
    bl_label = "Object to Wire"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.object.draw_type = 'WIRE'
        return {'FINISHED'}
    
#solid draw    
class SolidDraw(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.solid_draw"
    bl_label = "Object to Solid"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.object.draw_type = 'SOLID'
        return {'FINISHED'}

#textured
class TexDraw(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tex_draw"
    bl_label = "Object to Texture"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.object.draw_type = 'TEXTURED'
        return {'FINISHED'}
    
#wire draw toggle test
class WireToggle(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.wire_toggle"
    bl_label = "Toggle Wire"
 
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
 
    def execute(self, context):
        if bpy.context.object.draw_type == 'SOLID':
            bpy.context.object.draw_type = 'WIRE'
        elif bpy.context.object.draw_type == 'WIRE':
            bpy.context.object.draw_type = 'SOLID'
        else: 
            bpy.context.object.draw_type = 'WIRE'
        return {'FINISHED'}

    
    
    
#------------------------------------#pie
class VIEW3D_PIE_drawtypes(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "DRAW TYPE"

    def draw(self, context):
        layout = self.layout
        
        pie = layout.menu_pie()
        #pie.operator("render.render", text='one')

        pie.operator("object.wire_frame", text='Wire', icon='GRID')
        pie.operator("object.solid_draw", text='Solid', icon='SNAP_VOLUME')
        pie.operator("object.tex_draw", text='Textured', icon='TEXTURE')
        pie.operator("object.wire_toggle", text='Wire Toggle', icon='SNAP_FACE')
        
        #Pie Select
        km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS', ctrl=True, alt=False)
        kmi.properties.name = "VIEW3D_PIE_drawtypes"
        




def register():
    bpy.utils.register_class(WireFrame)
    bpy.utils.register_class(TexDraw)
    bpy.utils.register_class(SolidDraw)
    bpy.utils.register_class(WireToggle)
    bpy.utils.register_class(VIEW3D_PIE_drawtypes)


def unregister():
    bpy.utils.unregister_class(WireFrame)
    bpy.utils.unregister_class(TexDraw)
    bpy.utils.unregister_class(SolidDraw)
    bpy.utils.unregister_class(WireToggle)
    bpy.utils.unregister_class(VIEW3D_PIE_drawtypes)


if __name__ == "__main__":
    register()
