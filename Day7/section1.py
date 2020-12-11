def FormatTxt():
    f = open('input.txt', 'r', encoding='UTF-8')
    data_lines = [s[:-2].replace(" contain ", ", ").split(", ") for s in f.readlines()]
    return data_lines

def GenerateBagArr(data_lines):
    bagarr = {}
    for line in data_lines:
        bagarr[line[0]] = line[1:]
    return bagarr

print(GenerateBagArr(FormatTxt()))

def PossibleBagConfiguration(bagarr):
    pass
