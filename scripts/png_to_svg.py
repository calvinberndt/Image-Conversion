#!/usr/bin/env python3
import base64
from PIL import Image
import sys
import os
import argparse

def png_to_svg(png_path, svg_path):
    # Open the PNG image to get dimensions
    with Image.open(png_path) as img:
        width, height = img.size
    
    # Read the PNG file and encode as base64
    with open(png_path, 'rb') as f:
        png_data = f.read()
    
    base64_data = base64.b64encode(png_data).decode('utf-8')
    
    # Create SVG content with embedded PNG
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
     width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <image x="0" y="0" width="{width}" height="{height}" 
         xlink:href="data:image/png;base64,{base64_data}"/>
</svg>'''
    
    # Write the SVG file
    with open(svg_path, 'w') as f:
        f.write(svg_content)
    
    print(f"Successfully converted {png_path} to {svg_path}")

def _resolve_input_path(input_arg):
    # If a path or absolute path is provided, use it directly
    if os.path.isabs(input_arg) or os.path.sep in input_arg:
        if not os.path.exists(input_arg):
            sys.exit(f"Input file not found: {input_arg}")
        return input_arg

    # Otherwise, look under the repository's images directory
    repo_root = os.path.dirname(os.path.dirname(__file__))
    images_dir = os.path.join(repo_root, "images")
    candidate = os.path.join(images_dir, input_arg)
    if not os.path.exists(candidate):
        sys.exit(f"Input file not found: {candidate}")
    return candidate

def _derive_output_path(input_path, output_arg):
    if output_arg:
        output_dir = os.path.dirname(output_arg)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        return output_arg
    base, _ = os.path.splitext(input_path)
    return base + ".svg"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PNG to an SVG (embedded PNG as base64)")
    parser.add_argument("input", help="PNG file name in images/ or a path to a PNG file")
    parser.add_argument("-o", "--output", help="Output SVG path (defaults to alongside input with .svg extension)")
    args = parser.parse_args()

    input_path = _resolve_input_path(args.input)
    if not input_path.lower().endswith(".png"):
        sys.exit("Only .png files are supported.")

    output_path = _derive_output_path(input_path, args.output)
    png_to_svg(input_path, output_path)
