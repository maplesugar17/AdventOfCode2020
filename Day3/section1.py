'''
right 3 down 1
'''
f = open('input.txt', 'r', encoding='UTF-8')
datalist = [s.strip() for s in f.readlines()]
requiredwidth = len(datalist)*3//len(datalist[0])+1
datalist = [s*requiredwidth for s in datalist]

for index, line in enumerate(datalist):
    datalist[index] = list(line)

x = 0
y = 0
treenum = 0
while y < len(datalist):
    if datalist[y][x] == "#":
        treenum += 1
    x += 3
    y += 1
print(treenum)
