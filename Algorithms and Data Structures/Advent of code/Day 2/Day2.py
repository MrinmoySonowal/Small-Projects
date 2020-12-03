def parse_line(line):
    w1 = line.split(" ")
    numbers = [int(i) for i in w1[0].split("-")]
    letter = w1[1][0]
    word = w1[2]
    return numbers, letter, word


def get_num_of_valid_passcodes(fileName):
    f = open(fileName, "r")
    count = 0
    for line in f:
        range_limits, letter, word = parse_line(line)
        if (word.count(letter) >= range_limits[0]) and (word.count(letter) <= range_limits[1]):
            count += 1
    f.close()
    return count


def get_num_of_valid_pass_TCAS(fileName):
    f = open(fileName, "r")
    count = 0
    for line in f:
        indices, letter, word = parse_line(line)
        if (word[indices[0] - 1] == letter) ^ (word[indices[1] - 1] == letter):  # Used exclusive or as our condition is only true when exactly one of them is true
            count += 1
    f.close()
    return count

