from glob import glob
from PIL import Image
import os
import sys

os.chdir("/home/lorenzo/Immagini/DoA")

for picture in glob("*.tga"):
    outfile = os.path.splitext(picture)[0] + ".png"

    try:
        print "Converting: ", picture
        Image.open(picture).save(outfile)
    except IOError as detail:
	print "    * Conversion failed for this file.", detail
