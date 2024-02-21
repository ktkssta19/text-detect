

import easyocr
import cv2
import os
import re

# Function to extract numeric part from a string
def extract_numeric_part(s):
    match = re.search(r'\d+', s)
    return int(match.group()) if match else 0

# Placeholder for input and output folder paths
input_folder = 'ImagesGrayscales'
output_folder = 'ImgBoundingBox'
output_folder2 = 'ImgCropped'
output_folder3 = 'ImgTextFileBB'

# Urdu and English both language model
reader = easyocr.Reader(['ur', 'en'], gpu=False)

# Process images in the input folder
for filename in sorted(os.listdir(input_folder), key=extract_numeric_part):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Adjust file extensions as needed
        file_path = os.path.join(input_folder, filename)

        # Loading Image
        img = cv2.imread(file_path)
        
        # Read text
        results = reader.readtext(img, detail=1, paragraph=False)

        # Create a TextFile1 for each image
        textfile1_name = os.path.splitext(filename)[0] + ".txt"
        textfile1_path = os.path.join(output_folder3, textfile1_name)
        
        

        with open(textfile1_path, 'w') as textfile1:
            for i, (bbox, text, prob) in enumerate(results):
                # Define bounding boxes
                (tl, tr, br, bl) = bbox
                tl = (int(tl[0]), int(tl[1]))
                br = (int(br[0]), int(br[1]))

                # Save cropped images to OutputFolder2
                cropped_img = img[tl[1]:br[1], tl[0]:br[0]]
                cropped_img_filename = os.path.splitext(filename)[0] + "_C" + f"{i}" + ".jpg"
                cropped_output_path = os.path.join(output_folder2, cropped_img_filename)
                
                if not cropped_img.any():
                    print(f"Warning: Cropped image is empty for {cropped_img_filename}")
                    continue  # Skip saving if the image is empty
                
                cv2.imwrite(cropped_output_path, cropped_img)

                # Write bounding box coordinates to the TextFile1
                textfile1.write(f"{cropped_img_filename} : [{tl[0]},{tl[1]}] , [{tr[0]},{tr[1]}] , [{bl[0]},{bl[1]}] , [{br[0]},{br[1]}] \n")
                
                
    
                
                
        # Draw bounding boxes on the original image in a separate loop
        for bbox in results:
            (tl, tr, br, bl) = bbox[0]
            tl = (int(tl[0]), int(tl[1]))
            br = (int(br[0]), int(br[1]))

            # For text, draw a blue bounding box on the original image
            cv2.rectangle(img, tl, br, (255, 0, 0), 2)

        # Save the modified image with bounding boxes in the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, img)
        
        print(f"File Done : {filename}")
