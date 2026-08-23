import xml.etree.ElementTree as ET
from PIL import Image
import os

ET.register_namespace('', "http://www.w3.org/2000/svg")

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

def remove_bg(svg_path, original_jpg_path, output_path=None):
    if output_path is None:
        base, _ = os.path.splitext(svg_path)
        output_path = f"{base}_nobg.svg"
        
    img = Image.open(original_jpg_path)
    # Use (50, 50) to avoid any rounded corners or borders
    bg_color = img.getpixel((50, 50)) 
    
    print(f"Detected background color: {bg_color}")

    tree = ET.parse(svg_path)
    root = tree.getroot()
    paths = root.findall('.//{http://www.w3.org/2000/svg}path')
    
    if not paths:
        return output_path
        
    removed_count = 0
    for p in paths:
        fill = p.attrib.get('fill')
        if fill:
            try:
                c = hex_to_rgb(fill)
                if color_distance(c, bg_color) < 30:
                    root.remove(p)
                    removed_count += 1
                else:
                    # In cutout mode, shapes don't overlap. We add a slight stroke 
                    # to close the anti-aliasing gaps between adjacent paths.
                    p.attrib['stroke'] = fill
                    p.attrib['stroke-width'] = "1"
                    p.attrib['stroke-linejoin'] = "round"
            except ValueError:
                pass
                
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"Removed {removed_count} background paths.")
    return output_path

if __name__ == "__main__":
    import sys
    remove_bg(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
