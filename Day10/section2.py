from collections import Counter

def FormatTxt():
    f = open('input.txt', 'r', encoding='UTF-8')
    data_lines = [int(line.rstrip()) for line in f.readlines()]
    return data_lines

def AdaptersPattern(data_lines):
    sol = {0:1}
    for line in sorted(data_lines):
        sol[line] = 0
        if line - 1 in sol:
            sol[line]+=sol[line-1]
        if line - 2 in sol:
            sol[line]+=sol[line-2]
        if line - 3 in sol:
            sol[line]+=sol[line-3]
    return sol[max(data_lines)]

print(AdaptersPattern(FormatTxt()))
