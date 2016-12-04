import os
import ast
import time
cwd = os.getcwd()
dir_list = os.listdir(cwd)

files_to_merge = [f for f in dir_list if "out.txt" in f]
print files_to_merge
a_list = [[]] * (64 ** 3)

if "merge_out.txt" in files_to_merge:
    files_to_merge.remove("merge_out.txt")
    files_to_merge = ["merge_out.txt"] + files_to_merge

for f in files_to_merge:
    fi = open(f,"r")
    print time.strftime("%H:%M:%S " + f)
    for i, l in enumerate(fi):
        #if i % 10000 == 0 : print f + ", " + str(i)
        line = ast.literal_eval(l.replace("\n",""))
        if len(line) > 0:
            if len(a_list[i]) == 0:
                a_list[i] = list(line)
            else:
                for j in range(len(line)):
                    for k in range(len(a_list[i])):
                        if a_list[i][k][0] == line[j][0]:
                            a_list[i][k][1] = a_list[i][k][1] + line[j][1]
                            #print "hit " + str(a_list[i])
                            break
                    else:
                        a_list[i] = a_list[i] + [line[j]]
    fi.close()
    os.remove(f)
fo = open("MERGE.txt","w")
for k in a_list:
    fo.write(str(k) + "\n")
