import os
from PIL import Image

def generate_wallpaper():
    assets_dir = "assets"
    images_list = [
        "10_Base_Smile.jpg", "11_Base_Wink.jpg", "12_Base_Happy.jpg", "13_Base_Surprised.jpg", "14_Base_Angry.jpg",
        "15_Base_Crying.jpg", "16_Base_Dizzy.jpg", "17_Base_Starry.jpg", "18_Base_Sleepy.jpg", "19_Base_Love.jpg",
        "20_Base_Blep.jpg", "21_Base_Cool.jpg", "22_Base_Sweating.jpg", "23_Base_Shadow.jpg", "24_Base_Pleading.jpg"
    ]
    
    for img_name in images_list:
        img_path = os.path.join(assets_dir, img_name)
        if not os.path.exists(img_path):
            print(f"Error: {img_path} not found!")
            return

    images = [Image.open(os.path.join(assets_dir, img_name)) for img_name in images_list]
    
    target_width = 3840
    target_height = 2160
    
    # 无缝平铺
    tile_size = target_height // 3 # 720
    
    resized_images = [img.resize((tile_size, tile_size), Image.Resampling.LANCZOS) for img in images]
    
    # 按照你的要求，填充一个类似于 #9BD8B6 的底色
    # #9BD8B6 的 RGB 值是 (155, 216, 182)
    bg_color = (155, 216, 182)
    
    # 创建 16:9 画布
    wallpaper = Image.new("RGB", (target_width, target_height), bg_color)
    
    # 计算左侧偏移量以确保整体居中，左右会露出 #9BD8B6 的底色来填补 16:9 的空白
    offset_x = (target_width - (5 * tile_size)) // 2
    offset_y = 0
    
    # 拼接图片 (无间距)
    for index, img in enumerate(resized_images):
        row = index // 5
        col = index % 5
        x = offset_x + col * tile_size
        y = offset_y + row * tile_size
        wallpaper.paste(img, (x, y))
        
    output_path = "Kigurumi_16x9_Wallpaper.jpg"
    wallpaper.save(output_path, quality=95)
    print(f"Success! Seamless wallpaper with #9BD8B6 background saved to {output_path}")

if __name__ == "__main__":
    generate_wallpaper()
