import ast
fi = open("MERGE.txt","r")

edge_count = 0
for i,l in enumerate(fi):
    l = l.replace("\n","")
    line = ast.literal_eval(l)
    for x in line:
        edge_count += x[1]
edge_count =  edge_count * 2

b = (2 * 4) + (4 * 70 * 3) + (70 * 70 * 4)


print "Total number of edges counted : " + str(edge_count)
print "Number of edges per website : " + str(b)
print "Number of websites : " + str(edge_count / b)