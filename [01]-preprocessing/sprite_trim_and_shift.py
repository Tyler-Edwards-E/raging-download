
from PIL import Image, ImageChops
from hueshift import shift_hue
import numpy as np
import os

spritedir = r"example/ken-sprites" # Folder with raw sprites
newdir = r"example/ken-sprites-shift" # Folder where you want the edited sprites to go (
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
    diff = ImageChops.add(diff, diff, 0.001, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

print("Running...")

# Getting average sprite size so any outliers can be resized to match
sumw = 0
sumh = 0
c = 0
for subdir, dirs, files in os.walk(spritedir):
    for file in files:
        image_file = Image.open(os.path.join(subdir, file))
        image_trim = trim(image_file)
        image_size = image_trim.size
        sumw = sumw + image_size[0]
        sumh = sumh + image_size[1]
        c = c + 1

avgw = int(sumw / c)
avgh = int(sumh / c)

print()
print("Image Count", c)
print("Average Width", avgw)
print("Average Height", avgh)
print()
print("==========================================================================================")
print()
for subdir, dirs, files in os.walk(spritedir):
    print(subdir.split("\\")[-1])
    for file in files:
        print("     ", file)
        move_folder = newdir + "\\" + subdir.split("\\")[-1] # Create folder for that move's animations
        if not os.path.exists(move_folder):
            os.makedirs(move_folder)

        image_file = Image.open(os.path.join(subdir, file))

        # TRIM
        image_trim = trim(image_file)
        if image_trim.size[0] > avgw*2 or image_trim.size[1] > avgh*2: # Resize the original image and retrim if the sprite is too large (2x avg)
            image_file =  image_file.resize((avgw + 100,avgh + 100))
            image_trim = trim(image_file)
            print("         Resizing ->",subdir.split("\\")[-1], ",", file)
        image_trim.save(os.path.join(move_folder, "trim" + file)) # saves image result into new file

        # # 50% OPACITY
        # # To try and train for moves where characters fade away
        # img_opac = image_trim.copy()
        # img_opac.putalpha(128)
        # img_opac.save(os.path.join(move_folder, "opac" + file)) # saves image result into new file

        # GRAYSCALE
        img_grayscale = image_trim.convert('LA')
        img_grayscale.save(os.path.join(move_folder, "gray" + file)) # saves image result into new file

        # RAINBOW
        img_arr = np.array(image_trim.convert('RGBA'))
        for i in rainbowshift:
            img_rainbow = Image.fromarray(shift_hue(img_arr, rainbowshift[i]), 'RGBA')
            img_rainbow.save(os.path.join(move_folder, i + file))

