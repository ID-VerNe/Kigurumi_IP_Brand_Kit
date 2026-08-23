import vtracer
import os
from .config import VTRACER_OPTIONS
from .background_remover import remove_bg

def convert_jpg_to_svg(input_path, output_path=None):
    """Converts a raster image to SVG using vtracer."""
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.svg"
        
    print(f"Tracing vector for {input_path} -> {output_path}")
    vtracer.convert_image_to_svg_py(
        input_path,
        output_path,
        **VTRACER_OPTIONS
    )
    return output_path

def remove_svg_background(svg_path, original_jpg_path, output_path=None):
    return remove_bg(svg_path, original_jpg_path, output_path)
