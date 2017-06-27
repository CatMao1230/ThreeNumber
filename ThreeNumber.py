x = []
with open("arr.dat") as fo:
	while 1:
	    line = fo.readline()
	    if line == "":
	        break
	    line = line[:len(line) - 1]
	    x.append(line)

x.sort()
for i in range(-1, -4, -1):
	print x[i]