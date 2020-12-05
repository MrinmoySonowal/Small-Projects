def get_num(line, start, end,isRow):
    l = line[start:end]  # Remove \n
    if isRow:
        binary_str = l.replace('F', '0').replace('B', '1')
    else:
        binary_str = l.replace('L', '0').replace('R', '1')
    return int(binary_str, 2)


f = open('input.txt', 'r')
seat_Ids = []
for line in f:
    row_num = get_num(line, 0, -4,True)
    col_num = get_num(line, -4, -1,False)
    seat_Ids.append(row_num*8+col_num)
# a
print(max(seat_Ids))
seat_Ids.sort()
for i in range(len(seat_Ids)-1):
    if (seat_Ids[i+1] - seat_Ids[i]) == 2:
        # b
        print(seat_Ids[i]+1)
        break
