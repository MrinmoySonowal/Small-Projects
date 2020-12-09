#1
def twoSum(list, target):
    """
    Here we find a pair of values from the list that sum to the target
    """
    for item in list:
        if (target - item) in list:
            return True
    return False

f = open("input.txt", "r")
lines = [int(line[:-1]) for line in f.readlines()]
for i in range(25,len(lines)):
    if not twoSum(lines[i-25:i], lines[i]):
        print(lines[i])
        break
f.close()


#2
def contiguous_sum(lines, number):
    i = 1
    arr = [lines[0]]
    sum = arr[0]
    while arr[0] != lines[-1]:
        if sum > number:
            sum -= arr[0]
            del arr[0]
        elif sum == number:
            return max(arr) + min(arr)
        else:
            arr.append(lines[i])
            sum += lines[i]
            i += 1



f = open("input_1.txt", "r")
lines = [int(line[:-1]) for line in f.readlines()]
print(contiguous_sum(lines,542529149))
