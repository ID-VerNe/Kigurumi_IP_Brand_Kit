import os
from PIL import Image

def remove_white_corners(img):
    img = img.convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    # 扫描四个角 (这里假定圆角的范围不会超过 60x60)
    corner_size = 60
    for x in range(w):
        for y in range(h):
            if (x < corner_size or x >= w - corner_size) and (y < corner_size or y >= h - corner_size):
                r, g, b, a = pixels[x, y]
                # 识别接近纯白的像素并将其变为透明
                if r > 240 and g > 240 and b > 240:
                    pixels[x, y] = (r, g, b, 0)
    return img

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

    # 打开图片，并处理掉白色的圆角
    images = []
    for img_name in images_list:
        img = Image.open(os.path.join(assets_dir, img_name))
        img = remove_white_corners(img)
        images.append(img)
    
    target_width = 3840
    target_height = 2160
    
    tile_size = target_height // 3 # 720
    
    # 调整尺寸，注意此时因为图片有 Alpha 通道，需要小心处理
    resized_images = [img.resize((tile_size, tile_size), Image.Resampling.LANCZOS) for img in images]
    
    # 背景色设为匹配的薄荷绿
    bg_color = (155, 216, 182)
    
    # 创建 16:9 画布
    wallpaper = Image.new("RGBA", (target_width, target_height), bg_color + (255,))
    
    offset_x = (target_width - (5 * tile_size)) // 2
    offset_y = 0
    
    # 拼接图片，由于图片带有 alpha 通道，需要将其作为 mask 传入进行透明混合
    for index, img in enumerate(resized_images):
        row = index // 5
        col = index % 5
        x = offset_x + col * tile_size
        y = offset_y + row * tile_size
        wallpaper.paste(img, (x, y), img)
        
    output_path = "Kigurumi_16x9_Wallpaper.jpg"
    # 保存为 JPG 前先转换为 RGB
    wallpaper = wallpaper.convert("RGB")
    wallpaper.save(output_path, quality=95)
    print(f"Success! Wallpaper with transparent corners handled saved to {output_path}")

if __name__ == "__main__":
    generate_wallpaper()
