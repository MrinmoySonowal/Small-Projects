# Program to print n palindrome numbers:
# if n == 2:
# we need to print 
# 1 
# 121      
# if n == 5: 
# 1
# 121
# 12321
# 1234321
# 123454321    


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i)//9)**2)
 