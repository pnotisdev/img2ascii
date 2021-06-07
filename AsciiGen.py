from PIL import Image, ImageDraw
import math

from pip._vendor.distlib.compat import raw_input

characters = "1234567890abcdefghijklmnopqrstuvwxyz"[::-1] #Change these characters to whatever you want
charArray = list(characters)
charLength = len(charArray)
interval = charLength / 256
scaleFactor = 0.20 #Change scale
oneCharWidth = 10 #Character width
oneCharHeight = 10 #Character height


def get_character(inputint):
    return charArray[math.floor(inputint * interval)]


text_file = open("Output.txt", "w") #Outputs to output.txt

image = raw_input("Enter the name of the image file: ")
image = Image.open(image) #opens image
width, height = image.size #width + height = the image size
image = image.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))),
                     Image.NEAREST) #resizes depending on the variables
width, height = image.size
pixel = image.load() #loads image

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(25, 14, 20)) #Background color will be hex #190e14 or rgb(25, 14, 20)
draw = ImageDraw.Draw(outputImage) #draws the outputted image

for i in range(height):
    for j in range(width):
        r, g, b = pixel[j, i]
        h = int(r / 3 + g / 3 + b / 3)
        pixel[j, i] = (h, h, h)
        text_file.write(get_character(h)) #writes the ascii into text file
        draw.text((j * oneCharWidth, i * oneCharHeight), get_character(h), fill=(r, g, b)) #fills

    text_file.write('\n')

outputImage.save('output.png') #Outputs to png image
