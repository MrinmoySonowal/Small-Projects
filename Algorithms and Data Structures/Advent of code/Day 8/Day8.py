def get_acc(lines):
    acc = 0
    visited_indices = []
    i = 0
    while True:
        if i in visited_indices:
            return visited_indices
        visited_indices.append(i)
        val_split = lines[i].split(' ')
        if val_split[0] == 'nop':
            i += 1
        elif val_split[0] == 'acc':
            acc += int(val_split[1])
            i += 1
        elif val_split[0] == 'jmp':
            i += int(val_split[1])
        elif val_split[0] == 'end':
            return acc


def reach_end_acc(lines, visited_indices):
    for i in visited_indices:
        b = lines[:]

        if 'jmp' in b[i]:
            b[i] = b[i].replace('jmp','nop')
            n = get_acc(b)
            if type(n) is int:
                print(n)
        if 'nop' in b[i]:
            b[i] = b[i].replace('nop','jmp')
            n = get_acc(b)
            if type(n) is int:
                print(n)

f = open('input.txt', 'r')
lines = [line[:-1] for line in f.readlines()]
visited_i = get_acc(lines)
reach_end_acc(lines, visited_i)
