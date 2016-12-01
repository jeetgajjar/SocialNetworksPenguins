
from selenium import webdriver
from PIL import Image
import os
import csv
import time
import numpy as np


start_time = time.time()
driver = webdriver.PhantomJS()
driver.set_window_size(720, 720)
imagename = 'line.png'


with open('test.csv', 'rb') as csvfile:

    x = 0
    y = 0
    list_pixel = []
    for line in csvfile:
        driver.get(line)
        driver.save_screenshot('line.png')
        im = Image.open('line.png').convert('RGB')

        #This block prints all pixels (time should be ~15 seconds/img)
        pixel = im.load()
        for x in xrange(0, 720, 10):

            for y in xrange(0, 720, 10):
                list_pixel = pixel[x, y]

                #prints all 3-tuples, skipping 10 pixels
                print list(list_pixel)
                array = np.asarray(list_pixel)
                for i in array:
                    print i


                # with open('colorGraph.csv', 'w'):
                #     csv.writer

                #Need to create adjacency list from 720x720 list


        # black, white = im.getcolors()
        # blue, green = im.getcolors()
        # red = im.getcolors()

        # for x in range(720):
        #     for y in range(720):
        #         color = im.getpixel((x, y))
        #     print(color)
        # for black, white, blue, green, red in im:
        #
        # print ('black: ', black[0])
        # print ('white: ', white[0])
        # print ('blue: ', blue[0])
        # print ('green: ', green[0])
        # print ('red: ', red[0])
        # print



        #Maybe create an if-statement to connect the colors together?
        #Each pixel will have 2-3 neighbors
        end_time = time.time()
    final_time = end_time - start_time
    print "Total time:", final_time

