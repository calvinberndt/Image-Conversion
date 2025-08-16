# Image Conversions

This repository provides Python scripts for converting PNG images to SVG format, with optional background removal. The scripts are designed to help you embed PNG images into SVG containers, either as-is or with transparent backgrounds, making them suitable for web and design workflows.

## Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
  - [png_to_svg.py](#png_to_svgpy)
  - [png_to_svg_with_bg_removal.py](#png_to_svg_with_bg_removalpy)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic PNG to SVG](#basic-png-to-svg)
  - [PNG to SVG with Background Removal](#png-to-svg-with-background-removal)
- [Directory Structure](#directory-structure)
- [Notes](#notes)
- [License](#license)

---

## Overview

This project contains two main scripts:

- **png_to_svg.py**: Converts a PNG image to an SVG file by embedding the PNG as a base64-encoded image within the SVG.
- **png_to_svg_with_bg_removal.py**: Removes the background from a PNG image using AI, then embeds the result as a base64-encoded image in an SVG.

Both scripts use the [Pillow](https://python-pillow.org/) library for image processing. The background removal script also uses [rembg](https://github.com/danielgatis/rembg).

---

## Scripts

### `png_to_svg.py`

- **Purpose**: Converts a PNG image to an SVG file by embedding the PNG as a base64-encoded image.
- **How it works**:
  - Reads the PNG file.
  - Gets its dimensions.
  - Encodes the PNG in base64.
  - Creates an SVG file with the PNG embedded as an `<image>` element.

- **CLI**:
  - Run: `python scripts/png_to_svg.py <input_png> [-o OUTPUT_SVG]`
  - If `<input_png>` is a bare filename (e.g., `phoenix.png`), it is resolved under the repository's `images/` directory.
  - If `-o/--output` is omitted, the output `.svg` is written alongside the input with the same basename.

---

### `png_to_svg_with_bg_removal.py`

- **Purpose**: Removes the background from a PNG image and converts it to an SVG with the transparent PNG embedded.
- **How it works**:
  - Reads the PNG file.
  - Uses `rembg` to remove the background.
  - Gets the dimensions of the processed image.
  - Encodes the result in base64.
  - Creates an SVG file with the processed PNG embedded as an `<image>` element.

- **Default behavior**: Looks for `WiSys.png` and `SparkSymposium.png` in the current directory, processes them if found, and outputs `WiSys.svg` and `SparkSymposium.svg`.

---

## Requirements

- Python 3.7+
- [Pillow](https://python-pillow.org/)
- [rembg](https://github.com/danielgatis/rembg) (for background removal script)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/image_conversions.git
   cd image_conversions
   ```

2. **Install dependencies:**
   ```bash
   pip install pillow rembg
   ```

---

## Usage

### Basic PNG to SVG

To convert a PNG to SVG without background removal using the CLI:

```bash
# Use a bare filename (looked up in images/)
python scripts/png_to_svg.py phoenix.png

# Use an explicit path to the PNG
python scripts/png_to_svg.py images/phoenix.png

# Specify a custom output SVG path
python scripts/png_to_svg.py images/phoenix.png -o images/phoenix.svg

# Show help
python scripts/png_to_svg.py -h
```

Notes:
- Only `.png` inputs are supported.

### PNG to SVG with Background Removal

To remove the background and convert to SVG:

```bash
python scripts/png_to_svg_with_bg_removal.py
```

- By default, this script looks for `WiSys.png` and `SparkSymposium.png` in the current directory.
- To process other files, modify the `main()` function in `png_to_svg_with_bg_removal.py`:
  ```python
  remove_background_and_convert_to_svg('your_input.png', 'your_output.svg')
  ```

---

## Directory Structure

```
image_conversions/
  images/                # Place your PNG images here (optional)
  scripts/
    png_to_svg.py
    png_to_svg_with_bg_removal.py
```

---

## Notes

- The output SVG files contain the PNG image as a base64-encoded `<image>` element. This does **not** vectorize the image; it simply embeds the PNG in an SVG container.
- For true vectorization (tracing), consider using tools like [potrace](http://potrace.sourceforge.net/) or [Inkscape's trace bitmap](https://inkscape.org/doc/tutorials/tracing/tutorial-tracing.html).
- The background removal uses AI and may not be perfect for all images.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
