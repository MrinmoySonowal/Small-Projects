import math


def LCMofArray(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    return lcm


def GCDofArray(b):
    if len(b) == 2: return math.gcd(b[0], b[1])
    return math.gcd(b[0], GCDofArray(b[1:]))


def getTotalX(a, b):
    # Write your code here
    lcm = LCMofArray(a)
    print(lcm)
    gcd = GCDofArray(b)
    i = lcm
    ctr = 0
    while i <= gcd:
        if gcd % i == 0:
            ctr += 1
        i += lcm
        print(i)
    return ctr


tot = getTotalX([2, 3, 6], [42, 84])
print(tot)
