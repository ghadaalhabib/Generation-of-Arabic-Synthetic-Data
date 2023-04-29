# Generation-of-Arabic-Synthetic-Data
This repository offers a guide to generate Arabic synthetic data using different Arabic fonts to perform data augmentation to improve the performance of machine learning models or to train an OCR software.

![0](https://user-images.githubusercontent.com/67872328/235325407-76cf473e-322d-425c-a1b3-fd33902cf7f6.jpg)
![34](https://user-images.githubusercontent.com/67872328/235325416-ce57b20d-8713-4c45-aa96-62c31f672499.jpg)
![36](https://user-images.githubusercontent.com/67872328/235325424-dba14ce1-57a1-4e80-abd0-f2c7c5e7bf92.jpg)
![37](https://user-images.githubusercontent.com/67872328/235325426-0e92bb49-6b0a-40dd-9431-a0f657740067.jpg)


The following GitHub Repository was used to perform data synthesis: Text Recognition Data Generator
https://github.com/Belval/TextRecognitionDataGenerator

Additional documentation:
https://textrecognitiondatagenerator.readthedocs.io/en/latest/

Notes: 

1- TextRecognitionDataGenerator2.py should assist you in generating images using Arabic. Arabic is not fully supported by the package for some fonts.

Add the fonts to be used in the trdg folder (use only .ttf because TextRecognitionDataGenerator only works with this type of font)
You can download the fonts online or use the fonts available in the font book initially installed  
Add the font names without the .ttf extension line by line in a text file

2- Choose the font you wish to generate the images: Go to the TextRecognitionDataGenerator folder -> trdg -> fonts
    
3- Add the text you need to generate images of in a text file in the "trdg" folder, not the "dict" folder to generate the images in the same order as the text file. Otherwise, not specifying the text file and only using the ar file in the "dict" folder will generate images in a random order.

4- Move to the trdg folder and run the run.py script. 

Check the description of the arugments available in the documentation. I personally ran the following comand to generate images in Arabic: python3 run.py -l ar -c 48 -na 2 --input_file ar2.txt
(Make sure you delete the hidden files in the font folder there before you run anything)

5- TextRecognitionDataGenerator file will assist you if you need to add the images in an excel sheet in the same order as the text file.
