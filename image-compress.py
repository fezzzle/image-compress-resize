from PIL import Image, ImageOps
import sys
import os
import re

# To run this script, you need to pass 4 arguments:
# 1. The path to the directory containing the images you want to resize
# 2. The path to the directory where you want to save the resized images
# 3. The width of the resized images
# 4. The height of the resized images
# python3 image-compress.py /home/mp/Downloads/click-and-grow/cg-UC-partners-products ./uc-resized-images/ 2540 1920


file_extensions = (".jpg", ".jpeg", ".png")
size = (int(sys.argv[3]), int(sys.argv[4]))

def is_valid_dir_name(dir_name):
    # This regular expression checks if the dir_name is a valid directory name
    # It doesn't allow any special characters except for - and _
    return re.match("^(?=.*[a-zA-Z_/.-])[a-zA-Z0-9_/.-]*$", dir_name) is not None


def create_dir():
    number_of_dirs = 0
    # Pass the first argument as its the name of the script
    for i, argument in enumerate(sys.argv[1:]):
        print("ARGUMENT IS:", argument, i)
        if os.path.isdir(argument):
            print("path exist and is dir", argument)
        elif is_valid_dir_name(argument):
                os.makedirs(argument)
                number_of_dirs += 1
                print("Directory '% s' created" % argument)
        else:
            print("Invalid directory name:", argument)

def compress_image():
    for filename in os.listdir(sys.argv[1]):
        print("Filename:", filename)
        full_path = os.path.join(sys.argv[1], filename)
        if os.path.isfile(full_path) and filename.endswith(file_extensions):
            sanitized_filename = filename.replace(" ", "_").lower() 
            with Image.open(full_path) as img:
                resized_img = ImageOps.contain(img, size)
                resized_img.save(os.path.join(sys.argv[2], "resized_" + sanitized_filename))

try:
    create_dir()
    compress_image()
except OSError as error:
    print("Error:", error)







