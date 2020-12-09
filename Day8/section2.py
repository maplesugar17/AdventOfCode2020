def FormatTxt():
    f = open('input.txt', 'r', encoding='UTF-8')
    data_lines = [s.strip() for s in f.readlines()]
    # data_lines = [s.split(" ") for s in data_lines]
    # del data_lines[-1][-1]
    return data_lines

acc = 0
def Execute(codes):
    global acc
    acc = 0
    index = 0
    executedindex = []
    currentcode = ""
    flag = False
    while True:
        if index in executedindex:
            print("repeated")
            break
        else:
            executedindex.append(index)
            currentcode = codes[index]
            if index >= len(codes) - 1:
                if "nop" in currentcode or currentcode == "jmp +1":
                    print("有効")
                    flag = True
                    break
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
    return flag

def TryChangeCode(codes):
    for num, code in enumerate(codes):
        tmpcode = list(codes)
        if "nop" in code:
            tmpcode[num] = code.replace("nop", "jmp")
        elif "jmp"in code:
            tmpcode[num] = code.replace("jmp", "nop")

        if Execute(tmpcode) == True:
            print(acc)
            break

TryChangeCode(FormatTxt())
