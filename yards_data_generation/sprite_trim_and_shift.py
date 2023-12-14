
from PIL import Image, ImageChops
from hueshift import shift_hue
import numpy as np
import os

spritedir = r"C:\Users\Ty\3D Objects\~RD\Data Generation\YARDS-UNI2\Nanase - Copy" # Folder with raw sprites
newdir = r"C:\Users\Ty\3D Objects\~RD\Data Generation\YARDS-UNI2\nanasetest" # Folder where you want the edited sprites to go (
if not os.path.exists(newdir): # Will create newdir if you didn't already
    os.makedirs(newdir)

redshift = (180 - 180) / 360.0
orangeshift = (90 - 65)/360.0
yellowshift = (180-360)/360.0
greenshift = (300 - 180) / 360.0
blueshift = (400-180)/360.0
purpleshift = (360 - 90)/360.0

rainbowshift = {"red":redshift, "orange":orangeshift, "yellow":yellowshift, "green":greenshift, "blue":blueshift, "purple":purpleshift}

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 0.1, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

print("Running...")
for subdir, dirs, files in os.walk(spritedir):
    for file in files:

        move_folder = newdir + "\\" + subdir.split("\\")[-1] # Create folder for that move's animations
        if not os.path.exists(move_folder):
            os.makedirs(move_folder)

        image_file = Image.open(os.path.join(subdir, file))

        # TRIM
        image_trim = trim(image_file)
        image_trim.save(os.path.join(move_folder, "trim" + file)) # saves image result into new file
        # image_trim.save(os.path.join(subdir, "trim" + file)) # saves image result into new file

        # GRAYSCALE
        img_grayscale = image_trim.convert('LA')
        img_grayscale.save(os.path.join(move_folder, "gray" + file)) # saves image result into new file
        # img_grayscale.save(os.path.join(subdir, "gray" + file)) # saves image result into new file

        # RAINBOW
        img_arr = np.array(image_trim.convert('RGBA'))
        for i in rainbowshift:
            img_rainbow = Image.fromarray(shift_hue(img_arr, rainbowshift[i]), 'RGBA')
            img_rainbow.save(os.path.join(move_folder, i + file))
            # img_rainbow.save(os.path.join(subdir, i + file))