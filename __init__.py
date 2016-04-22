# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Drawtype Operator Pie",
           "author": "CDMJ",
           "version": (1, 0, 0),
           "blender": (2, 77, 0),
           "location": "",
           "description": "Drawtype per object changing in 3d View",
           "warning": "Not usable in TexPaint mode",
           "category": "3D View"}






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
