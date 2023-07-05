import bpy
from mathutils import *
from math import *
import os



 
file_loc_1 = r"C:\Users\ASUS\Desktop\Work\Blender script\medium_body_animation"
Files = os.listdir(file_loc_1)
for File1 in Files:
    body_path = os.path.join(file_loc_1,File1)
    
    name1 = File1.rsplit('.', 1)[0]  
     
     
    
    file_loc_2 = r"C:\Users\ASUS\Desktop\Work\Blender script\Tshirt_dataset_5"
    Files = os.listdir(file_loc_2)
    for File2 in Files:
        cloth_path = os.path.join(file_loc_2,File2)
        
        name2 = File2.rsplit('_', 1)[0]
        name3 = File2.rsplit('_',1)[1]
        name4 = name3.rsplit('.',1)[0]
         
        
        if name1 == name2:
        
             
            #import 35 animation
            imported_object_body = bpy.ops.wm.alembic_import(filepath=body_path)
            obj_object_body = bpy.context.selected_objects[0]
            bpy.context.scene.frame_start = 0
            bpy.context.scene.frame_end = 307
            
            bpy.context.scene.render.fps = 30
            
            #select body
            bpy.context.view_layer.objects.active = obj_object_body

            #add collision properties to body
            bpy.ops.object.modifier_add(type='COLLISION')
            bpy.context.object.collision.thickness_outer = 0.1
            bpy.context.object.collision.cloth_friction = 80
            
            #import  tshirt
            imported_object_cloth = bpy.ops.import_scene.obj(filepath=cloth_path)
            obj_object_cloth = bpy.context.selected_objects[0] 
             

            #select cloth
            bpy.context.view_layer.objects.active = obj_object_cloth
             
            #add cloth properties
            bpy.ops.object.modifier_add(type='CLOTH')
            bpy.ops.object.modifier_add(type='COLLISION')
#            bpy.context.object.collision.thickness_outer = 0.1
#            bpy.context.object.collision.cloth_friction = 80
            
            bpy.context.object.modifiers["Cloth"].settings.quality = 15
            bpy.context.object.modifiers["Cloth"].settings.time_scale = 1.2
            bpy.context.object.modifiers["Cloth"].settings.mass = 0.1
            bpy.context.object.modifiers["Cloth"].settings.tension_stiffness = 15.0
            bpy.context.object.modifiers["Cloth"].settings.compression_stiffness = 6
            bpy.context.object.modifiers["Cloth"].settings.shear_stiffness = 1
            bpy.context.object.modifiers["Cloth"].settings.bending_stiffness = 0.5
            bpy.context.object.modifiers["Cloth"].settings.compression_damping = 3
            bpy.context.object.modifiers["Cloth"].settings.shear_damping = 1
            bpy.context.object.modifiers["Cloth"].settings.tension_damping = 3.0
            bpy.context.object.modifiers["Cloth"].settings.bending_damping = 0.1            
            bpy.context.object.modifiers["Cloth"].point_cache.frame_end = 307
            bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 6
            bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
            

            
            #run simulator
            bpy.context.scene.frame_set(-1) 
            for i in range(307):
                bpy.context.scene.frame_set(bpy.context.scene.frame_current + 1)   
                if i > 23:             
                    file_loc=f"C:\\Users\\ASUS\\Desktop\\Work\\Blender script\\animation_medium\\{name1}_{name4}\\{name1}_{name4}_{i-24}.obj"
                    bpy.ops.export_scene.obj(filepath=file_loc , use_selection=True ,use_materials=False, global_scale=.033334 , use_mesh_modifiers = True)
                    
                
                
#            for obj in bpy.context.scene.objects:
#                if obj.type == 'MESH' and obj.name.startswith("P"):
#                    obj.name = "tshirt" 
#                
#            for obj in bpy.context.scene.objects:
#                if obj.type == 'mesh':
#                    obj.name = "armature"
#                    
#                object_to_delete = bpy.data.objects['armature']  # delete armature
#                bpy.data.objects.remove(object_to_delete, do_unlink=True)
                
            for obj in bpy.context.scene.objects:   #rename selected object
#                if obj.type == 'MESH' :
                obj.name = "tshirt"
                object_to_delete = bpy.data.objects['tshirt']      # delete cloth
                bpy.data.objects.remove(object_to_delete, do_unlink=True)
                 
#            for obj in bpy.context.scene.objects:    #rename selected object
##                 if obj.type == 'MESH':
#                    obj.name = "body"
#                     
#                 object_to_delete = bpy.data.objects['body']     # delete body
#                 bpy.data.objects.remove(object_to_delete, do_unlink=True)
#            
       