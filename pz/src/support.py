import os  
import pygame  


#用于寻找角色相关动作图片的路径
#————————————————————————————————————————————————————————————
def import_assets():  
    pygame.init()
    animations = {  
        'left': [], 'right': [], 'right_idle': [],  
        'left_idle': [],   
        'left_up': [], 'right_up': [] ,'right_updown': [],'left_updown':[]
    }  
  
    for animation, folder in animations.items():
        # 获取脚本文件的绝对路径  
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        parent_dir = os.path.dirname(script_dir)
  
        # 构造到 'graphics/character/' 的绝对路径  
        graphics_dir = os.path.join(parent_dir, 'graphics', 'character')
        full_path = os.path.join(graphics_dir,animation)
        if not os.path.exists(full_path):
           print(f"Error: The directory '{full_path}' does not exist.")
        surface_list = []  
        # 注意这里，我们不再在循环内部修改 full_path  
        for dirpath, _, img_files in os.walk(full_path):
            for image in img_files:
                # 使用 os.path.join 来构造完整的图片文件路径
                img_path = os.path.join(dirpath, image)
                image_surf = pygame.image.load(img_path).convert_alpha()
                surface_list.append(image_surf)
        animations[animation] = surface_list
  
    return animations


