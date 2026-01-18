# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Comparable",
    "author": "FFuthoni",
    "description": "Compare two objects or collections in one click",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "location": "View 3D -> Side Panel -> Comparable",
    "warning": "",
    "category": "3D View",
}

import bpy
import rna_keymap_ui

addon_keymaps= []

def cmpr_props(opt):
    scene_prop= bpy.context.scene.cmpr_scene_prop
    if opt == 'prop':
        return scene_prop
    elif opt == 'obj1':
        return scene_prop.obj1
    elif opt == 'obj2':
        return scene_prop.obj2
    elif opt == 'col1':
        return scene_prop.col1
    elif opt == 'col2':
        return scene_prop.col2
    elif opt == 'obj_rndr':
        return scene_prop.obj_rndr
    elif opt == 'col_rndr':
        return scene_prop.col_rndr

def cmpr_prefs(opt):
    pref_prop= bpy.context.preferences.addons[__package__].preferences
    if opt == 'pref':
        return pref_prop
    elif opt == 'tab':
        return pref_prop.tab

def cmpr_update_sidebar(self, context):
    try:
        for panel in panels:
            bpy.utils.unregister_class(panel)
    except:
        pass

    for panel in panels:
        panel.bl_category= self.category
        bpy.utils.register_class(panel)

class CMPR_SceneProps(bpy.types.PropertyGroup):
    obj1: bpy.props.PointerProperty(name='Comparable Object 1', type=bpy.types.Object)
    obj2: bpy.props.PointerProperty(name='Comparable Object 2', type=bpy.types.Object)
    col1: bpy.props.PointerProperty(name='Comparable Collection 1', type=bpy.types.Collection)
    col2: bpy.props.PointerProperty(name='Comparable Collection 2', type=bpy.types.Collection)

    obj_rndr: bpy.props.BoolProperty(name='Comparable Affect Objects Render Visibilty',
                                     description="Affect the Objects' render visibility",
                                     default=False,
                                     )
    col_rndr: bpy.props.BoolProperty(name='Comparable Affect Collections Render Visibilty',
                                     description="Affect the Collections' render visibility",
                                     default=False,
                                     )

class CMPR_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname= __package__

    tab: bpy.props.EnumProperty(
        items=(
            ('CHANGELOG', 'Changelogs', ''),
            ('KEYMAP', 'Keymaps', ''),
        ),
        default='CHANGELOG')
    
    category: bpy.props.StringProperty(
        name="Sidebar Category Name",
        description="Set sidebar category name in case you want to move it to another category",
        default='Comparable',
        update= cmpr_update_sidebar,
    )

    def draw(self, context):
        layout= self.layout

        layout.prop(self, 'category')

        row= layout.row()
        row.prop(self, 'tab', expand=True)
        if self.tab == 'CHANGELOG':
            layout.label(text='Changelog: V1.0.0 - 13-01-26 : ', icon='LINENUMBERS_ON')
            layout.label(text='--- Addon creation')
        else:
            layout.label(text='All keymaps are deactivated by default to avoid conflict with your setup. You can change them to your liking before activating them.')
            layout.label(text='To restore deleted keymaps, just reload the addon. But it is better to use the checkboxes to disable them')

            col= layout.column()
            kc= context.window_manager.keyconfigs.user
            km= kc.keymaps['3D View']
            for kmi in km.keymap_items:
                if 'cmpr.' in kmi.idname:
                    col.context_pointer_set("keymap", km)
                    rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)

class CMPR_OT_CompareObjs(bpy.types.Operator):
    """
    Compare two objects by alternating their viewport visibility
    """
    bl_label= 'Comparable_CompareObjects'
    bl_idname= 'cmpr.cmpr_objs'
    bl_options= {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj1= cmpr_props('obj1')
        obj2= cmpr_props('obj2')

        if obj1 == None or obj2 == None:
            cls.poll_message_set("Two objects need to be selected!")
            return False   
        elif obj1 == obj2:
            cls.poll_message_set("The same object cannot be selected twice!")
            return False
        
        return True

    def execute(self, context):
        obj1= cmpr_props('obj1')
        obj2= cmpr_props('obj2')

        if not ((obj1 == None) or (obj2 == None)):
            if obj2.hide_viewport:
                obj1.hide_viewport= True
                obj2.hide_viewport= False
                if cmpr_props('obj_rndr'):
                    obj1.hide_render= True
                    obj2.hide_render= False
            else:
                obj1.hide_viewport= False
                obj2.hide_viewport= True
                if cmpr_props('obj_rndr'):
                    obj1.hide_render= False
                    obj2.hide_render= True
        else:
            self.report({'ERROR'}, message="Two objects need to be selected!")
        
        return {"FINISHED"}

class CMPR_OT_ResetObjs(bpy.types.Operator):
    """
    Reset both objects to be visible
    """
    bl_label= 'Comparable_ResetObjects'
    bl_idname= 'cmpr.reset_objs'
    bl_options= {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj1= cmpr_props('obj1')
        obj2= cmpr_props('obj2')

        if obj1 == None or obj2 == None:
            cls.poll_message_set("Two objects need to be selected!")
            return False   
        elif obj1 == obj2:
            cls.poll_message_set("The same object cannot be selected twice!")
            return False
        
        return True

    def execute(self, context):
        obj1= cmpr_props('obj1')
        obj2= cmpr_props('obj2')

        if not ((obj1 == None) or (obj2 == None)):
            obj1.hide_viewport= False
            obj2.hide_viewport= False
            if cmpr_props('obj_rndr'):
                obj1.hide_render= False
                obj2.hide_render= False
        else:
            self.report({'ERROR'}, message="Two objects need to be selected!")
        
        return {"FINISHED"}

class CMPR_OT_CompareCols(bpy.types.Operator):
    """
    Compare two collections by alternating their viewport visibility
    """
    bl_label= 'Comparable_CompareCollections'
    bl_idname= 'cmpr.cmpr_cols'
    bl_options= {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        col1= cmpr_props('col1')
        col2= cmpr_props('col2')

        if col1 == None or col2 == None:
            cls.poll_message_set("Two collections need to be selected!")
            return False   
        elif col1 == col2:
            cls.poll_message_set("The same collection cannot be selected twice!")
            return False
        
        return True

    def execute(self, context):
        col1= cmpr_props('col1')
        col2= cmpr_props('col2')

        if not ((col1 == None) or (col2 == None)):
            if col2.hide_viewport:
                col1.hide_viewport= True
                col2.hide_viewport= False
                if cmpr_props('col_rndr'):
                    col1.hide_render= True
                    col2.hide_render= False
            else:
                col1.hide_viewport= False
                col2.hide_viewport= True
                if cmpr_props('col_rndr'):
                    col1.hide_render= False
                    col2.hide_render= True
        else:
            self.report({'ERROR'}, message="Two collections need to be selected!")
        
        return {"FINISHED"}

class CMPR_OT_ResetCols(bpy.types.Operator):
    """
    Reset both collections to be visible
    """
    bl_label= 'Comparable_ResetCollections'
    bl_idname= 'cmpr.reset_cols'
    bl_options= {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        col1= cmpr_props('col1')
        col2= cmpr_props('col2')

        if col1 == None or col2 == None:
            cls.poll_message_set("Two collections need to be selected!")
            return False   
        elif col1 == col2:
            cls.poll_message_set("The same collection cannot be selected twice!")
            return False
        
        return True

    def execute(self, context):
        col1= cmpr_props('col1')
        col2= cmpr_props('col2')

        if not ((col1 == None) or (col2 == None)):
            col1.hide_viewport= False
            col2.hide_viewport= False
            if cmpr_props('col_rndr'):
                    col1.hide_render= False
                    col2.hide_render= False
        else:
            self.report({'ERROR'}, message="Two collections need to be selected!")
        
        return {"FINISHED"}

class CMPR_PT_CompareObjs(bpy.types.Panel):
    bl_label= 'Compare Objects'
    bl_idname= 'CMPR_PT_CompareObjs'
    bl_space_type= 'VIEW_3D'
    bl_region_type= 'UI'
    bl_category= 'Comparable'

    def draw_header(self, context):
        layout= self.layout
        layout.label(icon='OBJECT_DATA')

    def draw(self, context):
        obj1= cmpr_props('obj1')
        obj2= cmpr_props('obj2')

        layout= self.layout

        layout.label(text='Object 1')
        row_obj1= layout.row()
        row_obj1.prop(cmpr_props('prop'),
                    'obj1',
                    text= "",
                    icon= 'OBJECT_DATA' if obj1 == None else 'RESTRICT_VIEW_ON' if obj1.hide_viewport else 'RESTRICT_VIEW_OFF',
                    )
        if obj1 is not None:
            row_obj1.label(icon='RESTRICT_RENDER_ON' if obj1.hide_render else 'RESTRICT_RENDER_OFF')
        
        layout.label(text='Object 2')
        row_obj2= layout.row()
        row_obj2.prop(cmpr_props('prop'),
                    'obj2',
                    text="",
                    icon= 'OBJECT_DATA' if obj2 == None else 'RESTRICT_VIEW_ON' if obj2.hide_viewport else 'RESTRICT_VIEW_OFF',
                    )
        if obj2 is not None:
            row_obj2.label(icon='RESTRICT_RENDER_ON' if obj2.hide_render else 'RESTRICT_RENDER_OFF')

        layout.operator('cmpr.cmpr_objs', text='Switch', emboss=True)
        layout.operator('cmpr.reset_objs',text='Reset', emboss=True)

        layout.prop(cmpr_props('prop'),
                    'obj_rndr',
                    text="Affect Render")

class CMPR_PT_CompareCols(bpy.types.Panel):
    bl_label= 'Compare Collections'
    bl_idname= 'CMPR_PT_CompareCols'
    bl_space_type= 'VIEW_3D'
    bl_region_type= 'UI'
    bl_category= 'Comparable'

    def draw_header(self, context):
        layout= self.layout
        layout.label(icon='OUTLINER_COLLECTION')

    def draw(self, context):
        col1= cmpr_props('col1')
        col2= cmpr_props('col2')

        layout= self.layout

        layout.label(text='Collection 1')
        row_col1= layout.row()
        row_col1.prop(cmpr_props('prop'),
                    'col1',
                    text= "",
                    icon= 'OUTLINER_COLLECTION' if col1 == None else 'RESTRICT_VIEW_ON' if col1.hide_viewport else 'RESTRICT_VIEW_OFF',
                    )
        if col1 is not None:
            row_col1.label(icon='RESTRICT_RENDER_ON' if col1.hide_render else 'RESTRICT_RENDER_OFF')

        layout.label(text='Collection 2')
        row_col2= layout.row()
        row_col2.prop(cmpr_props('prop'),
                    'col2',
                    text="",
                    icon= 'OUTLINER_COLLECTION' if col2 == None else 'RESTRICT_VIEW_ON' if col2.hide_viewport else 'RESTRICT_VIEW_OFF',
                    )
        if col2 is not None:
            row_col2.label(icon='RESTRICT_RENDER_ON' if col2.hide_render else 'RESTRICT_RENDER_OFF')

        layout.operator('cmpr.cmpr_cols', text='Switch', emboss=True)
        layout.operator('cmpr.reset_cols', text='Reset', emboss=True)

        layout.prop(cmpr_props('prop'),
                    'col_rndr',
                    text="Affect Render")

panels=[
    CMPR_PT_CompareObjs,
    CMPR_PT_CompareCols,
]

classes= [
    CMPR_PT_CompareObjs,
    CMPR_OT_CompareObjs,
    CMPR_OT_ResetObjs,
    CMPR_PT_CompareCols,
    CMPR_OT_CompareCols,
    CMPR_OT_ResetCols,
    CMPR_AddonPreferences,
]

def register():
    bpy.utils.register_class(CMPR_SceneProps)
    bpy.types.Scene.cmpr_scene_prop= bpy.props.PointerProperty(type=CMPR_SceneProps)

    for cls in classes:
        bpy.utils.register_class(cls)

    wm= bpy.context.window_manager
    kc= wm.keyconfigs.addon
    if kc:
        km= kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi= km.keymap_items.new('cmpr.cmpr_objs', type='BACK_SLASH', value='PRESS')
        kmi.active= False
        addon_keymaps.append((km, kmi))
        kmi= km.keymap_items.new('cmpr.cmpr_cols', type='BACK_SLASH', value='PRESS', shift=True)
        kmi.active= False
        addon_keymaps.append((km, kmi))
        kmi= km.keymap_items.new('cmpr.reset_objs', type='BACK_SLASH', value='PRESS', alt=True)
        kmi.active= False
        addon_keymaps.append((km, kmi))
        kmi= km.keymap_items.new('cmpr.reset_cols', type='BACK_SLASH', value='PRESS', shift=True, alt=True)
        kmi.active= False
        addon_keymaps.append((km, kmi))
    
def unregister():
    bpy.utils.unregister_class(CMPR_SceneProps)
    del bpy.types.Scene.cmpr_scene_prop

    for cls in classes:
        bpy.utils.unregister_class(cls)

    try:
        for km, kmi in addon_keymaps:
            if km.space_type != 'PROPERTIES':
                km.keymap_items.remove(kmi)
            else:
                print("Comparable: Keymaps found in space type 'PROPERTIES' which could throw errors, removing skipped")
        addon_keymaps.clear()
    except RuntimeError:
        pass

if __name__ == "__main__":
    register()

