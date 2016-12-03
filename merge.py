import os
import ast
cwd = os.getcwd()
dir_list = os.listdir(cwd)
files_to_merge = [f for f in dir_list if "out.txt" in f]

a_list = [[]] * (64 ** 3)

for f in files_to_merge:
    for i, l in enumerate(f):
        line = ast.literal_eval(l.replace("\n",""))
        print len(line)
        if len(line) > 0:
            print line[0]
    break