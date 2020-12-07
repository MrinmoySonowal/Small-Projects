# 1
def search(fileName, word):
    f = open(fileName, "r")
    output = ""
    for line in f:
        line_split = line.split(" bags contain ")
        if word in line_split[1]:
            output += line_split[0] + "-" + search(fileName, line_split[0])
    f.close()
    return output


# 2
def search_num_bags(fileName, word):
    count = 0
    f = open(fileName, "r")
    for line in f:
        line_split = line.split(" bags contain ")
        if word in line_split:
            line_split[1] = line_split[1].replace('.\n', '')
            if "no other bags" in line_split[1]:
                return 0
            for str in line_split[1].split(", "):
                if str[-1] == 's':
                    count += int(str[0]) + int(str[0]) * search_num_bags("input.txt", str[2:-5])
                else:
                    count += int(str[0]) + int(str[0]) * search_num_bags("input.txt", str[2:-4])
    f.close()
    return count


str = search("input.txt", "shiny gold")
print(len(set(str.split("-"))))

print(search_num_bags('input.txt', 'shiny gold'))
