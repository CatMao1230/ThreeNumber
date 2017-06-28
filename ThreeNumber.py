import sys

def access_from_file(file):
    x = []
    with open(file) as fo:
        while True:
            line = fo.readline()
            if line == "":
                break
            line = line.strip()
            x.append(line)
    return x

def find_three_max(x):

    ls = [0, 0, 0]
    for i in x:
        for index, element in enumerate(ls[:3]):
            if i > element:
                ls.insert(index, i)
                break
    return ls[:3]

if __name__ == '__main__':
    find_three_max(access_from_file(sys.argv[1]))