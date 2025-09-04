import cv2
import argparse
import os

def resize_image(source: str, destination: str, scale_percent: int = 50) -> None:
    """
    Resizes an image by a given percentage and saves it to a new file.

    Parameters:
    -----------
    source : str
        Path to the input image file.
    destination : str
        Path where the resized image will be saved.
    scale_percent : int
        Percentage of original size to scale (default: 50).
    """

    #Load image
    image =  cv2.imread(source, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(f"Image not found at {source}")
    # cv2.imshow("title", image)
   
    new_width=int(image.shape[1] * scale_percent/100)
    new_height=int(image.shape[0] * scale_percent/100)

    #resize image
    output=cv2.resize(image,(new_width,new_height))
    cv2.imwrite(destination, output)
    print(f"Image saved at {destination} with size {new_width}x{new_height}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize an image by percentage")
    parser.add_argument("source", help="Path to input image")
    parser.add_argument("destination", help="Path to save resized image")
    parser.add_argument("--scale", type=int, default=50, help="Scaling percentage (default: 50)")
    
    args = parser.parse_args()
    resize_image(args.source, args.destination, args.scale)
# cv2.waitKey(0)