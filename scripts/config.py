# Shared configuration for Kigurumi SVG converter

VTRACER_OPTIONS = {
    "colormode": "color",
    "hierarchical": "cutout",     # Changed to cutout for perfect background removal
    "mode": "spline",
    "filter_speckle": 2,          
    "color_precision": 8,         
    "layer_difference": 4,        
    "corner_threshold": 60,
    "length_threshold": 4.0,
    "max_iterations": 10,
    "splice_threshold": 45,
    "path_precision": 8
}
