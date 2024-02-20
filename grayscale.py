# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:04:32 2024

@author: ktksa
"""

import os
import cv2

def convert_to_grayscale(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    files = os.listdir(input_folder)
    image_files = [file for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

    for image_file in image_files:
        # Read the image
        image_path = os.path.join(input_folder, image_file)
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save the grayscale image
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, gray_img)

        print(f"Converted {image_file} to grayscale and saved as {image_file} in the output folder.")

# Replace 'input_folder_path' with your desired input folder containing images
input_folder_path = 'C:/Users/ktksa/.spyder-py3/Images'
output_folder_path = 'C:/Users/ktksa/.spyder-py3/ImagesGrayscale'


convert_to_grayscale(input_folder_path,output_folder_path)
