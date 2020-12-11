from collections import Counter

def FormatTxt():
    f = open('input.txt', 'r', encoding='UTF-8')
    data_lines = [int(s) for s in f.readlines()]
    return data_lines

def TestAdapters(data_lines):


print(TestAdapters(FormatTxt()))
