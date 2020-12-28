import os
import sys

path = sys.argv[1]

if not os.path.exists(path):
    os.makedirs(path)

for x in range(int(sys.argv[2])):
    filename = os.path.join(path, str(x))
    print(filename)
    f = open(filename, "w")
    f.write("content for file %d" % (x))
    f.close()    

    f = open(filename, "r")
    print(f.read())