f = open('input.txt', 'r', encoding='UTF-8')
datalist = [s.strip() for s in f.readlines()]

def halve(arr, Firstbit = True):
    if Firstbit:
        return arr[:(len(arr)-1)//2]
    if not Firstbit:
        return arr[(len(arr)-1)//2+1:]

max = 0
for line in datalist:
    rowrange = range(128)
    for i in range(6):
        if line[i] == "F":
            rowrange = halve(rowrange)
        else:
            rowrange = halve(rowrange, False)
    rownum = 0
    if line[6] == "F":
        rownum = list(rowrange)[0]
    elif line[6] == "B":
        rownum = list(rowrange)[0] + 1

    columnrange = range(8)
    for i in range(7,9):
        if line[i] == "R":
            columnrange = halve(columnrange, False)
        else:
            columnrange = halve(columnrange)
    columnnum = 0
    if line[9] == "L":
        columnnum = list(columnrange)[0]
    elif line[9] == "R":
        columnnum = list(columnrange)[0] + 1

    if max < rownum*8+columnnum:
        max = rownum*8+columnnum

print(max)
