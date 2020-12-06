f = open('input.txt', 'r', encoding='UTF-8')
datalist = list(map(int, f.readlines()))

flag = False
for i in datalist:
    for j in datalist:
        if i+j == 2020:
            print(i*j)
            flag = True
            break
    if flag:
        break
