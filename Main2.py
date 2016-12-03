#!/usr/bin/env python2

from selenium import webdriver
from PIL import Image
import time
import threading
import os
import shutil


def adde(li, a, b):
    x = min(a,b)
    y = a + b - x
    for i in range(len(li[x])):
        if li[x][i][0] == y:
            li[x][i][1] = li[x][i][1] + 1
        return
    li[x] = li[x] + [[y,1]]


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



class DataProcessor(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        cwd = os.getcwd()

        my_folder = cwd + "\\process_" + str(self.id) + "_folder"
        if not os.path.exists(my_folder):
            os.makedirs(my_folder)
        working_folder = cwd + "\\working_folder"

        a_list = [[]] * (64 ** 3)
        cur_count = 0
        while 1:
            working_list = os.listdir(working_folder)
            if len(working_list) == 1 and working_list[0] == "endendend.txt":
                print "Writing end to output file " + str(self.id) + "\n"
                file_output = open(my_folder + "\\" +time.strftime("%H_%M_%S_") + str(self.id) + "_out.txt","w")
                for l in a_list:
                    file_output.write(str(l) + "\n")
                file_output.close()

                break
            if str(self.id) + ".png" in working_list:
                try:
                    im = Image.open(working_folder + "\\" + str(self.id) + '.png').convert('RGB')
                except IOError:
                    print "IOERROR " + working_folder + ", " + os.listdir(working_folder)
                    continue
                pixel = im.load()
                list1 = []
                list2 = []
                for y in xrange(0, 720, 10):
                    for x in xrange(0, 720, 10):
                        list_pixel = pixel[x, y]
                        cur_x = x / 10
                        cur_y = y / 10
                        list1 += [compress(list_pixel)]
                        if cur_x != 0:
                            adde(a_list,list1[cur_x],list1[cur_x - 1])
                        if cur_y != 0:
                            adde(a_list, list1[cur_x], list2[cur_x])
                    list2 = list(list1)
                    list1 = []
                cur_count += 1
                os.remove(working_folder + "\\" + str(self.id) + '.png')
                if cur_count > 9:
                    cur_count = 0
                    print "Writing 10 to output file " + str(self.id) + "\n"
                    file_output = open(my_folder + "\\" +time.strftime("%H_%M_%S_") + str(self.id) + "_out.txt", "w")
                    for l in a_list:
                        file_output.write(str(l) + "\n")
                    file_output.close()
                    a_list = [[]]*(64 ** 3)



class LoadBalancer(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
    def run(self):
        cwd = os.getcwd()

        output_folder = cwd + "\\output_folder"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        working_folder = cwd + "\\working_folder"
        if not os.path.exists(working_folder):
            os.makedirs(working_folder)
        else:
            for file in os.listdir(working_folder):
                os.remove(working_folder + "\\" + file)


        image_folder = cwd + "\\image_folder"
        current = int(0)
        while 1:
            #print current
            working_list = os.listdir(working_folder)
            image_cache = os.listdir(image_folder)
            if len(image_cache) == 1 and image_cache[0] == "endendend.txt":
                open(working_folder + "\\endendend.txt", "w").close()
                break
            if len(image_cache) == 0:
                #print "sleeping"
                time.sleep(1)
                current = (current + 1) % 5
                continue
            if str(current) + ".png" in working_list:
                #print "non"
                time.sleep(1)
                current = (current + 1) % 5
                continue
            shutil.copy(image_folder + "\\" + image_cache[0], working_folder + "\\" + str(current) + ".png")
            os.remove(image_folder + "\\" + image_cache[0])
            current = (current + 1) % 5
            #print current




class DriverThread(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename
        self.log_file_name = time.strftime("%y_%m_%d_%H_%M_%S_log.txt")
    def log(self,message):
        print time.strftime("%c") + " : DRIVER THREAD : " + message
        try:
            f = open(self.log_file_name,"w")
            f.write(time.strftime("%c") + " : DRIVER THREAD : " + message + "\n")
            f.close()
        except Exception:
            print "ERROR ON DRIVER LOGGING"
    def run(self):
        bad_count = 0
        cwd = os.getcwd()
        image_folder = cwd + "\\image_folder"
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        else:
            for file in os.listdir(image_folder):
                os.remove(image_folder + "\\" + file)

        log_dir = cwd + "\\driver_log"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.log_file_name = log_dir + "\\" + self.log_file_name
        driver = webdriver.PhantomJS()
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        driver.set_window_size(720, 720)
        csv = open(self.filename,'r')
        for i, l in enumerate(csv):
            if i < 10000:
                continue
            if i > 10020:
                break
            for j in range(604800):
                number_caps_in_folder = len(os.listdir(image_folder))
                #print os.listdir(image_folder)
                #print number_caps_in_folder
                if number_caps_in_folder > 5:
                    #print "sleeping"
                    time.sleep(1)
                else:
                    #print "not sleeping"
                    site = l.replace("\n","")
                    self.log("Reading in #" + str(i) + ", " + site)
                    try:
                        driver.get(site)
                        driver.save_screenshot(image_folder + "\\" + str(i) + '_cap.png')
                    except Exception:
                        bad_count += 1
                        self.log("Unable to read " + str(i) + ", " + site + ", Running total = " + str(bad_count))
                    break
        driver.close()
        csv.close()
        open(image_folder + "\\endendend.txt","w").close()


start_time = time.time()
threads = []
driver_thread = DriverThread('top20k.csv')
driver_thread.start()
threads.append(driver_thread)
time.sleep(5)
load_balancer = LoadBalancer()
load_balancer.start()
threads.append(load_balancer)
time.sleep(10)
for i in range(5):
    k = DataProcessor(i)
    k.start()
    threads.append(k)

for th in threads:
    th.join()


print "Total time:", time.time() - start_time
