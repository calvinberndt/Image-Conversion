import os
import base64
from PIL import Image
from rembg import remove
import io

def remove_background_and_convert_to_svg(input_path, output_path):
    """
    Remove background from PNG and convert to SVG format
    """
    print(f"Processing {input_path}...")
    
    # Read the input image
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()
    
    # Remove background using rembg
    print("Removing background...")
    output_data = remove(input_data)
    
    # Convert to PIL Image to get dimensions
    img = Image.open(io.BytesIO(output_data))
    width, height = img.size
    
    # Convert to base64 for embedding in SVG
    img_base64 = base64.b64encode(output_data).decode('utf-8')
    
    # Create SVG content
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}" 
     height="{height}" 
     viewBox="0 0 {width} {height}">
    <image x="0" y="0" 
           width="{width}" 
           height="{height}" 
           xlink:href="data:image/png;base64,{img_base64}"/>
</svg>'''
    
    # Write SVG file
    with open(output_path, 'w') as output_file:
        output_file.write(svg_content)
    
    print(f"Successfully converted {input_path} to {output_path} with background removed")

def main():
    # Process WiSys.png
    if os.path.exists('WiSys.png'):
        remove_background_and_convert_to_svg('WiSys.png', 'WiSys.svg')
    else:
        print("WiSys.png not found")
    
    # Process SparkSymposium.png
    if os.path.exists('SparkSymposium.png'):
        remove_background_and_convert_to_svg('SparkSymposium.png', 'SparkSymposium.svg')
    else:
        print("SparkSymposium.png not found")

if __name__ == "__main__":
    main()
