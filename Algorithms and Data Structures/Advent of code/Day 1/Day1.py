def genList(fileName):
    """ 
    Generates the list of numbers from the given file
    """
    f = open(fileName,"r")
    return [int(x) for x in f]

def twoSum(list, target):
    """
    Here we find a pair of values from the list that sum to the target
    """
    for item in list:
        if (target - item) in list:
            return item, (target-item), (target-item)*item
    return None,None,None

def tripleSum(list,target):
# Since list is sorted, we can iterate from item+1 to end of list to find the pair
# our target would be (actual target - firstitem)
    for i,v in enumerate(list):
        item1,item2,p = twoSum(list[i:],(target-v))
        if item1:
            product = v*item1*item2
            return v,item1,item2,product

list = genList("input.txt")
item1,item2,product = twoSum(list,2020)
print("item1= {}, item2= {}, product= {}".format(item1,item2,product))

# Here we find a triad of items from the list that sum to the target        
list2 = [item for item in list if item<2000]
list2.sort()

item0,item1,item2,product = tripleSum(list2,2020)
print("item0= {}, item1= {}, item2= {}, product= {}".format(item0,item1,item2,product))



