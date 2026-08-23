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
    
    # 设定最终壁纸的高度为 4K 标准
    target_width = 3840
    target_height = 2160
    
    # 设定网格的间距 (Gap)
    gap = 60
    
    # 计算图片大小：(总高度 - 上下留白 - 2个垂直间距) / 3
    # 假设上下留白 margin_y = 120
    margin_y = 120
    tile_size = (target_height - (2 * margin_y) - (2 * gap)) // 3 # (2160 - 240 - 120) // 3 = 600
    
    # 调整图片尺寸
    resized_images = [img.resize((tile_size, tile_size), Image.Resampling.LANCZOS) for img in images]
    
    # 使用品牌色：暖米白 (Cardigan Cream) #F5F1E6 作为底色
    # 这样每个图片就会像一张张独立的卡片/拍立得一样排列，不会出现边缘粘连的突兀感
    bg_color = (245, 241, 230)
    
    # 创建 16:9 画布
    wallpaper = Image.new("RGB", (target_width, target_height), bg_color)
    
    # 计算左侧偏移量以确保整体居中
    # 5列图片宽度 + 4个水平间距
    total_grid_width = (5 * tile_size) + (4 * gap)
    offset_x = (target_width - total_grid_width) // 2
    offset_y = margin_y
    
    # 拼接图片
    for index, img in enumerate(resized_images):
        row = index // 5
        col = index % 5
        x = offset_x + col * (tile_size + gap)
        y = offset_y + row * (tile_size + gap)
        wallpaper.paste(img, (x, y))
        
    output_path = "Kigurumi_16x9_Wallpaper.jpg"
    wallpaper.save(output_path, quality=95)
    print(f"Success! Wallpaper with distinct grid saved to {output_path}")

if __name__ == "__main__":
    generate_wallpaper()
