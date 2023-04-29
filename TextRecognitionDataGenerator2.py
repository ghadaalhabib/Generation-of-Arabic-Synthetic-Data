#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Import the necessary packages
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from PIL import Image 
import arabic_reshaper
from bidi.algorithm import get_display
import os
from trdg.generators import (
    GeneratorFromStrings,
)

# Add the fonts to be used in the trdg folder (use only .ttf because TextRecognitionDataGenerator only works with this type of font)
# You can download the fonts online or use the fonts available in the font book initially installed  
# Add the font names without the .ttf extension line by line in a text file

# Read the list of fonts to be used from a text file
fontList = [x.strip() for x in open("fonts.txt").readlines()]

# Iterate over the fonts
for index, font in enumerate(fontList):
    # Create an instance of the ArabicReshaper class
    reshaper = arabic_reshaper.ArabicReshaper(
    arabic_reshaper.config_for_true_type_font(
        f"{font}.ttf",
        arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )
    # Add the text to be displayed in each image, line by line, in a text file in the trdg folder
    # Input string or text file and ensure proper display
    texts = [x.strip() for x in open("ar2.txt", encoding = "utf8").readlines()]
    texts = [get_display(reshaper.reshape(str(w))) for w in texts]
    
    # Create a folder for each font
    if not os.path.exists(font):
        os.makedirs(font)

    # Generate the image
    for cnt, x in enumerate(texts):
    # The generators use the same arguments as the CLI, only as parameters
        generator = GeneratorFromStrings(
            size=50,
            strings=[x],
            language="ar",
            fonts=[f"{font}.ttf"],
        )

        for img, lbl in generator:
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            cv2.imwrite(f"./{font}/{cnt}.jpg", img)
            break
        
        


# In[ ]:




