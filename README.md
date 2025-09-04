Image Resizer
-
A Python script to resize images using OpenCV, allowing users to scale images by a specified percentage and save the output to a new file. This tool demonstrates skills in Python, image processing, and command-line interface development, ideal for data analysts working with visual data.

Features
-
1. Resize images by a customizable percentage.
2. Command-line interface for easy integration into data workflows.
3. Robust error handling for invalid image paths.
4. Supports common image formats (e.g., PNG, JPEG).

Requirements
-
1. Python 3.6+
2. OpenCV (opencv-python)

Installation
-
1. Clone this repository:git clone https://github.com/HMirza2024/image-resizer.git
cd image-resizer


2. Install the required dependency:pip install opencv-python

Usage
-
1. Run the script from the command line with the following syntax:
2. python resize_image.py <source_image> <destination_image> [--scale <percentage>]


- <source_image>: Path to the input image file.
- <destination_image>: Path where the resized image will be saved.
- --scale <percentage>: Optional scaling percentage (default: 50).

Example
-
To resize an image to 75% of its original size:
python resize_image.py input.jpg output.jpg --scale 75

This will resize input.jpg to 75% of its original dimensions and save it as output.jpg.

Code Structure
-
resize_image.py: Core script with image resizing logic using OpenCV and argparse for command-line argument parsing.

Notes
-
This project uses the opencv-python library, which is freely available.
