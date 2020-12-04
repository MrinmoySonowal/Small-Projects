import re


def is_valid_passport(str):
    str_split = str.split(" ")
    str_set = set()
    for field in str_split:
        print(field)
        if 'byr' in field:
            n = int(field.split(":")[1])
            if 1920 <= n <= 2002:
                str_set.add(field.split(":")[0])
        elif 'iyr' in field:
            n = int(field.split(":")[1])
            if 2010 <= n <= 2020:
                str_set.add(field.split(":")[0])
        elif 'eyr' in field:
            n = int(field.split(":")[1])
            if 2020 <= n <= 2030:
                str_set.add(field.split(":")[0])
        elif 'hgt' in field:
            if 'cm' in (field.split(":")[1]):
                n = field.split(":")[1]
                if 150 <= int(n.split("c")[0]) <= 193:
                    str_set.add(field.split(":")[0])
            elif 'in' in (field.split(":")[1]):
                n = field.split(":")[1]
                if 59 <= int(n.split("i")[0]) <= 76:
                    str_set.add(field.split(":")[0])
        elif 'hcl' in field:
            pattern = re.compile("^#([0-9]|[a-f]){6,6}$")
            if bool(pattern.match(field.split(":")[1])):
                str_set.add(field.split(":")[0])
        elif 'ecl' in field:
            if field.split(":")[1] in "amb blu brn gry grn hzl oth":
                str_set.add(field.split(":")[0])
        elif 'pid' in field:
            pattern = re.compile("^\d{9}$")
            print(field.split(":")[1])
            if bool(pattern.match(field.split(":")[1])):
                str_set.add(field.split(":")[0])

    print(str_set)
    if 'cid' in str_set:
        str_set.remove('cid')
    if '' in str_set:
        str_set.remove('')
    return str_set == {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def count_valid_passports(fileName):
    f = open(fileName, 'r')
    passport_str = ""
    count = 0
    for line in f:
        if line == "\n":
            count += is_valid_passport(passport_str)
            passport_str = ""
        else:
            passport_str += line.replace('\n', ' ')
    f.close()
    return count


print("Number of valid passports: {}".format(count_valid_passports('input.txt')))
