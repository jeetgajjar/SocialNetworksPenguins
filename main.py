
from selenium import webdriver
from PIL import Image
import os
import csv
import time


driver = webdriver.PhantomJS()
driver.set_window_size(720, 720)
imagename = 'line.png'

start_time = time.time()
with open('test.csv', 'rb') as csvfile:

    x = 0
    y = 0
    for line in csvfile:
        driver.get(line)
        driver.save_screenshot('line.png')
        im = Image.open('line.png').convert('1')

        # black, white = im.getcolors()
        # blue, green = im.getcolors()
        # red = im.getcolors()
        for x in im:
            for y in im:
                r, g, b = im.getpixel((x, y))
                y+1
            x+1
            print(r, g, b)
        # print ('black: ', black[0])
        # print ('white: ', white[0])
        # print ('blue: ', blue[0])
        # print ('green: ', green[0])
        # print ('red: ', red[0])
        # print



        #Maybe create an if-statement to connect the colors together?
        #Each pixel will have 4 neighbors...
        end_time = time.time()
    final_time = end_time - start_time
    print ('total time', final_time)
        # once you save, process the image:

        ##
        # TODO: Process Block within for loop


        ##
        # TODO: update to CSV file
        # with open('colorGraph.csv', 'w') as colorGraph:
        #
        ##

# with Image.open(imagename) as im:
#             print(imagename, im.format, "%dx%d" % im.size, im.mode)
# TODO Get color Values
# TODO: Not necessary to calculate the average since geting colors isn't too bad for all images
# class PixelCounter(object):
#     # loop through each pixel and average rgb
#     def __init__(self, imagename):
#         self.pic = Image.open(imagename)
#         self.imgData = self.pic.load()
#         def averagePixels(self):
#             r, g, b = 0, 0, 0
#             count = 0
#             for x in xrange(self.pic.size[0]):
#                 for y in xrange(self.pic.size[1]):
#                     alpha = self.imgData[x,y]
#                     r += alpha[0]
#                     g += alpha[1]
#                     b += alpha[2]
#                     count += 1
#
#                     # Average
#                     return (r/count), (g/count), (b/count), count

