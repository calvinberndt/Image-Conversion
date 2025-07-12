#!/usr/bin/env python3
import base64
from PIL import Image
import sys

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

if __name__ == "__main__":
    png_to_svg("SparkSymposium1.png", "SparkSymposium1.svg")
