import bisect
def median(arr,d,m):
    if  (d%2) == 0:
        return sum(arr[m-1:m+1])/2
    else:
        return arr[m]
    
def activityNotifications(expenditure, d):
    count = 0
    arr = sorted(expenditure[:d])
    for i in range(d,len(expenditure)):
        if expenditure[i] >= 2*median(arr,d,d//2) :
            count +=1    
        print(arr[0] , arr[bisect.bisect_left(arr,expenditure[i-d])])  
        # Removing 2nd element from expenditure (note it is not the same as the arr[0] as arr is sorted) 
        del arr[bisect.bisect_left(arr,expenditure[i-d])]   
        # As arr is sorted, inserting element while keeping arr sorted
        bisect.insort(arr,expenditure[i]) 
    return count