from collections import Counter


def count_unique_yes(line):
    line = line.replace('\n', '')
    return len(set(line))

def count_total_yes_anyone(fileName):
    f = open(fileName, "r")
    l=''
    count=0
    for line in f:
        if line == "\n":
            count += count_unique_yes(l)
            l = ""
        else:
            l += line
    f.close()
    return count

def count_everyone_yes(fileName):
    f = open(fileName, 'r')
    count = 0
    flag = 1
    for line in f:
        if line == '\n':
            count += len(l)
            flag = 1
        else:
            line = line.replace('\n', '')
            if flag:
                l = Counter(line)
                flag = 0
            else:
                l = l & Counter(line)   # Counter('a') & Counter('a') = Counter({'a':2}), enables counting common yeses
    f.close()
    return count


print(count_total_yes_anyone('input.txt'))
print(count_everyone_yes('input.txt'))
