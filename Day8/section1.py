def FormatTxt():
    f = open('input.txt', 'r', encoding='UTF-8')
    data_lines = [s.strip() for s in f.readlines()]
    # data_lines = [s.split(" ") for s in data_lines]
    # del data_lines[-1][-1]
    return data_lines

def Execute(codes):
    acc = 0
    index = 0
    executedindex = []
    currentcode = ""
    while True:
        if index in executedindex:
            print(acc)
            break
        else:
            executedindex.append(index)
            currentcode = codes[index]
            # print(currentcode)
            opcode = currentcode.split(" ")[0]
            operand = int(currentcode.split(" ")[1])
            if opcode == "acc":
                acc += operand
                index += 1
            elif opcode == "jmp":
                index += operand
            else:
                index += 1

Execute(FormatTxt())
