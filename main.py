#!/usr/bin/env python2

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
csv_writer = csv.writer(open('colorGraph.csv', 'wb'))

max_key = 68719476736

hash = {}


def compress(array):
    red = array[0]
    green = array[1]
    blue = array[2]
    int_rep_color = ((red / 4) * (64 ** 2)) + ((green / 4) * 64) + (blue / 4)

    return int_rep_color


def decompress(int_rep_color):

    blue = (int_rep_color % 64) * 4
    green = ((int_rep_color / 64) % 64) * 4
    red = (int_rep_color / (64 ** 2)) * 4

    return red, green, blue


def edge_compression(source, target):

    return long(source) * 262144 + long(target)


def edge_decompression(int_rep_edge):

    target = int(int_rep_edge % 262144)
    source = int(int_rep_edge / 262144)

    return source, target


def look_left(list1, cur_x):
    list1[cur_x -1]

    return list1


def look_up(list2, cur_y):
    list1[cur_y -1]

    return list2


with open('test.csv', 'rb') as csvfile:
    x = 0
    y = 0
    list_pixel = []
    list1 = []
    list2 = []
    counter = 0

    for line in csvfile:
        driver.get(line)
        driver.save_screenshot('line.png')
        im = Image.open('line.png').convert('RGB')

        # This block prints all pixels (time should be ~15 seconds/img max)
        pixel = im.load()
        for y in xrange(0, 720, 10):
            for x in xrange(0, 720, 10):
                list_pixel = pixel[x, y]
                cur_x = x/10
                cur_y = y/10

                list1 += [compress(list_pixel)]

                if cur_x != 0:
                   cur_edge_compression = edge_compression(list1[cur_x], list1[cur_x - 1])
                   counter +=1

                   try:
                       hash[cur_edge_compression] += 1
                   except KeyError:
                       hash[cur_edge_compression] = 1

                if cur_y != 0:
                   cur_edge_compression = edge_compression(list1[cur_x], list2[cur_x])
                   counter +=1


                   try:
                       hash[cur_edge_compression] += 1
                   except KeyError:
                       hash[cur_edge_compression] = 1

            list2 = list(list1)
            list1 = []
    print counter


    csv_writer.writerow(hash.items())


end_time = time.time()
final_time = end_time - start_time
print "Total time:", final_time
