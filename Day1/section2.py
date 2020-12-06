f = open('input.txt', 'r', encoding='UTF-8')
datalist = list(map(int, f.readlines()))

flag = False
for i in datalist:
    for j in datalist:
        for k in datalist:
            if i+j+k == 2020:
                print(i*j*k)
                flag = True
                break
        if flag:
            break
    if flag:
        break
