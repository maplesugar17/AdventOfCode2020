from collections import Counter

f = open('input.txt', 'r', encoding='UTF-8')
datalist = [s.strip() for s in f.readlines()]

pw_constraints = []
for line in datalist:
    line_constraints = line.split(" ")
    line_constraints[1] = line_constraints[1].replace(":", "")
    pw_constraints.append(line_constraints)

count = 0
for constraint in pw_constraints:
    target = constraint[2]
    if target[int(constraint[0].split("-")[0])-1] == constraint[1] and target[int(constraint[0].split("-")[1])-1] != constraint[1]:
        count += 1
    elif target[int(constraint[0].split("-")[1])-1] == constraint[1] and target[int(constraint[0].split("-")[0])-1] != constraint[1]:
        count += 1
print(count)
