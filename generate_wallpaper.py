import os
from PIL import Image

def generate_wallpaper():
    assets_dir = "assets"
    # 我们要拼接的 15 张表情图的文件名列表（按顺序）
    images_list = [
        "10_Base_Smile.jpg", "11_Base_Wink.jpg", "12_Base_Happy.jpg", "13_Base_Surprised.jpg", "14_Base_Angry.jpg",
        "15_Base_Crying.jpg", "16_Base_Dizzy.jpg", "17_Base_Starry.jpg", "18_Base_Sleepy.jpg", "19_Base_Love.jpg",
        "20_Base_Blep.jpg", "21_Base_Cool.jpg", "22_Base_Sweating.jpg", "23_Base_Shadow.jpg", "24_Base_Pleading.jpg"
    ]
    
    # 检查图片是否都存在
    for img_name in images_list:
        img_path = os.path.join(assets_dir, img_name)
        if not os.path.exists(img_path):
            print(f"Error: {img_path} not found!")
            return

    # 读取所有图片
    images = [Image.open(os.path.join(assets_dir, img_name)) for img_name in images_list]
    
    # 获取原始单张图片的尺寸（假设全都是正方形且一样大）
    base_w, base_h = images[0].size
    
    # 我们设定最终壁纸的高度为 4K 标准 (2160p)
    target_height = 2160
    target_width = 3840 # 16:9
    
    # 5x3 网格，所以单张图片的尺寸应该是:
    tile_size = target_height // 3 # 720
    
    # 调整所有图片的尺寸
    resized_images = [img.resize((tile_size, tile_size), Image.Resampling.LANCZOS) for img in images]
    
    # 取第一张图的左上角像素点颜色作为背景色
    bg_color = resized_images[0].getpixel((0, 0))
    
    # 创建 16:9 的画布
    wallpaper = Image.new("RGB", (target_width, target_height), bg_color)
    
    # 计算左侧的偏移量，让 5x3 网格完美居中
    # 5 列的总宽度 = 5 * tile_size = 3600
    # 左右留白 = (3840 - 3600) / 2 = 120
    offset_x = (target_width - (5 * tile_size)) // 2
    
    # 拼接图片
    for index, img in enumerate(resized_images):
        row = index // 5
        col = index % 5
        x = offset_x + col * tile_size
        y = row * tile_size
        wallpaper.paste(img, (x, y))
        
    output_path = "Kigurumi_16x9_Wallpaper.jpg"
    wallpaper.save(output_path, quality=95)
    print(f"Success! Wallpaper saved to {output_path}")

if __name__ == "__main__":
    generate_wallpaper()
