import sys

def access_from_file(file):
    x = []
    with open(sys.argv[1]) as fo:
        while True:
            line = fo.readline()
            if line == "":
                break
            line = line.strip()
            x.append(line)
    return x

def find_three_max(x):

    #for i in range(3):
    #    max = -1
    #    for j in x:
    #        if j > max:
    #            max = j
    #    print max
    #    del x[x.index(max)]

    ls = [0, 0, 0]
    for i in x:
        for index, element in enumerate(ls[:3]):
            if i > element:
                ls.insert(index, i)
                break
    print ls[:3]
        

find_three_max(access_from_file(sys.argv[1]))