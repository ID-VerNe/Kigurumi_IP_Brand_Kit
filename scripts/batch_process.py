import os
import glob
import sys
from .svg_processor import convert_jpg_to_svg, remove_svg_background

def process_image(jpg_path, remove_bg=False):
    assets_dir = os.path.dirname(jpg_path)
    bg_dir = os.path.join(assets_dir, "svg_with_bg")
    nobg_dir = os.path.join(assets_dir, "svg_nobg")
    
    os.makedirs(bg_dir, exist_ok=True)
    if remove_bg:
        os.makedirs(nobg_dir, exist_ok=True)
        
    base_name = os.path.basename(jpg_path)
    name, _ = os.path.splitext(base_name)
    
    svg_bg_path = os.path.join(bg_dir, f"{name}.svg")
    svg_nobg_path = os.path.join(nobg_dir, f"{name}.svg")
    
    # Generate the SVG with background
    convert_jpg_to_svg(jpg_path, svg_bg_path)
    
    # Generate the SVG without background
    if remove_bg:
        remove_svg_background(svg_bg_path, jpg_path, svg_nobg_path)
        print(f"Created transparent version: {svg_nobg_path}")
        
    print(f"Finished processing {jpg_path}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Kigurumi SVG Conversion Tool")
    parser.add_argument("target", help="File path, or 'all' to process the entire assets directory")
    parser.add_argument("--remove-bg", action="store_true", help="Generate transparent SVG in svg_nobg/ directory")
    
    args = parser.parse_args()
    
    if args.target == "all":
        # Look for the assets directory relative to this script
        assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
        jpgs = glob.glob(os.path.join(assets_dir, "*.jpg"))
        for jpg in jpgs:
            process_image(jpg, args.remove_bg)
    else:
        # If absolute path is provided, it processes it in its containing directory
        process_image(os.path.abspath(args.target), args.remove_bg)

if __name__ == "__main__":
    main()
