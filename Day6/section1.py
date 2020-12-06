from collections import Counter

def FormatTxt():
    f = open('input.txt', 'r', encoding='UTF-8')
    data_lines = f.read()
    data_lines = data_lines.replace("\n\n", "あいうえお").replace("\n", " ").replace("あいうえお", "\n").split("\n")
    # data_lines = [s.split(" ") for s in data_lines]
    # del data_lines[-1][-1]
    return data_lines

counts = []
def SumCount(arr):
    count = 0
    for item in arr:
        hoge = item.replace(" ", "")
        counts.append(Counter(hoge))
        count += len(Counter(hoge))
    return count

print(SumCount(FormatTxt()))
