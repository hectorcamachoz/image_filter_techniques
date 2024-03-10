"""
test_image_filtering.py
"""

# Import the libraries needed
import cv2
import numpy as np
import sys
import argparse 


# Local librarie
import cvlib as cvl

# Define the function to apply the average filter on an image 
def average_filter(img:cv2) -> cv2:
    """
    Apply the average filter on the image

    Args: 
        img: The image to convert
    Returns
        img_filtered: The image after applying the average filter function
    """
    img_filtered = cv2.blur(img,(5,5))
    return img_filtered 

# Define the function to apply the median filter on an image 
def median_filter(img:cv2) -> cv2:
    """
    Apply the average filter on the image

    Args: 
        img: The image to convert
    Returns
        img_filtered: The image after applying the median filter function
    """
    img_filtered = cv2.medianBlur(img,5)
    return img_filtered

# Define the function to apply the gaussian filter on an image 
def gaussian_filter(img: cv2) -> cv2:
    """
    Apply the average filter on the image

    Args: 
        img: The image to convert
    Returns
        img_filtered: The image after applying the gaussian filter function
    """
    img_filtered = cv2.GaussianBlur(img,(5,5),0)
    return img_filtered

# Define the function to parse the command line arguments
def parse_user_data() -> argparse:

    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Apply image '
                                     'filtering')
    
    # Add arguments
    parser.add_argument('--input_image', 
                        type=str, 
                        required=True, 
                        help='Input image to be filtered')
    
    parser.add_argument('--filter_name',
                        type=str,
                        required=True,
                        help="Filter name used as Kernel"
                        " [average, gaussian, median]")
    args = parser.parse_args()
    
    # Return parsed data entered by the user
    return args

# Define the main function
def run_pipeline(args:argparse.Namespace)->None:
    """
    Run the main function to apply the specified filter
    """
    args = parse_user_data()
    # Load image
    img = cvl.read_image(args.input_image)
    filter = args.filter_name

    if filter == "average":
        img_filtered = average_filter(img)
        title = "Average Filter Image"
    elif filter == "median":
        img_filtered = median_filter(img)
        title = "Median Filter Image"
    elif filter == "gaussian":
        img_filtered = gaussian_filter(img)
        title = "Gaussian Filter Image"
        

    cvl.visualise_image(img, "Original Image")
    cvl.visualise_image(img_filtered, title)
    cvl.close_windows()

if __name__ == "__main__":
    args = parse_user_data()
    
    run_pipeline(args = args)
    print('Program finished! \n')
