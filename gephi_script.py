import csv
import numpy as np

curr_line = []
curr_array = []

with open('testMerge.txt', 'r+') as infile:
    for line in infile:
        line.split(",")
        curr_array = np.asarray(line)
        for index, x in np.ndenumerate(curr_array):
            print (index, x)
