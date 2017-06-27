import sys

x = []
with open(sys.argv[1]) as fo:
    while True:
        line = fo.readline()
        if line == "":
            break
        line = line.strip()
        x.append(line)

for i in range(3):
    max = -1
    for j in x:
        if j > max:
        	max = j
    print max
    del x[x.index(max)]