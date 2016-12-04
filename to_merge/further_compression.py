import ast
import time


def new_compress(array):
    red = array[0]
    green = array[1]
    blue = array[2]
    int_rep_color = ((red / 8) * (32 ** 2)) + ((green / 8) * 32) + (blue / 8)
    return int_rep_color


def decompress(int_rep_color):
    blue = (int_rep_color % 64) * 4
    green = ((int_rep_color / 64) % 64) * 4
    red = (int_rep_color / (64 ** 2)) * 4
    return [red, green, blue]


start_time = time.time()
original_list = []
fi = open("MERGE.txt","r")

for i, l in enumerate(fi):
    if i % 10000 == 0 : print str(time.time() - start_time) + ", " + str(i)
    original_list += [list(ast.literal_eval(l.replace("\n", "")))]

fi.close()

print "starting conversion"
new_list = [[]] * (32 ** 3)

for node, neighbors in enumerate(original_list):
    for edge in neighbors:
        a = new_compress(decompress(node))
        b = new_compress(decompress(edge[0]))
        weight = edge[1]
        for i in new_list[a]:
            if i[0] == b:
                i[1] += weight
                print "hit"
                break
        else:
            new_list[a] = new_list[a] + [[b,weight]]

fo = open("newnew.txt","w")
for i in new_list:
    fo.write(str(i) + "\n")
fo.close()