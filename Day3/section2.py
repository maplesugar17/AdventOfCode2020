'''
Right 1, down 1.
Right 3, down 1.
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''
f = open('input.txt', 'r', encoding='UTF-8')
datalist = [s.strip() for s in f.readlines()]

def TreeNumber(req_x, req_y):
    requiredwidth = len(datalist)*req_x//len(datalist[0])+1
    biome = [s*requiredwidth for s in datalist]

    for index, line in enumerate(biome):
        biome[index] = list(line)

    x = 0
    y = 0
    treenum = 0
    while y < len(biome):
        if biome[y][x] == "#":
            treenum += 1
        x += req_x
        y += req_y
    return treenum

print(TreeNumber(1, 1)*TreeNumber(3, 1)*TreeNumber(5, 1)*TreeNumber(7, 1)*TreeNumber(1, 2))
