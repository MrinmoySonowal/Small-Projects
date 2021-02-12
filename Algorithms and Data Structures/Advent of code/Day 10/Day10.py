f = open('input.txt', 'r')
input_arr = [0]
for i in f.readlines():
    input_arr.append(int(i))
input_arr.sort()
input_arr.append(input_arr[-1]+3)
count_3 = count_1 = 0
for i in range(len(input_arr)-1):
    if (input_arr[i+1] - input_arr[i] ) == 3:
        count_3 += 1
    elif (input_arr[i+1] - input_arr[i] ) == 1:
        count_1 += 1

#a
print(count_1*count_3)
print(input_arr)