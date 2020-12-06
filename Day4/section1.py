'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''
field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

f = open('input.txt', 'r', encoding='UTF-8')
data_lines = f.read()
data_lines = data_lines.replace("\n\n", "あいうえお").replace("\n", " ").replace("あいうえお", "\n").split("\n")
print(data_lines)

count = 0
flag = True
for line in data_lines:
    for f in field:
        if not f in line:
            flag = False
            break
    if flag == True:
        count += 1
    else:
        flag = True

print(count)
