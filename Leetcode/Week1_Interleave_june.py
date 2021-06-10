def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    if ((s1 + s2) == s3) or ((s2 + s1) == s3):
        return True
    i, j, k = 0, 0, 0
    n, m = 0, 0
    while k < len(s3) and i < len(s1) and s1[i] == s3[k]:
        k += 1
        i += 1
    k = 0
    while k < len(s3) and j < len(s2) and s2[j] == s3[k]:
        k += 1
        j += 1
    is_exec = False
    if i >= j:
        j = 0
        k = i
        n = 1
    else:
        i = 0
        k = j
        m = 1
    if i > j:
        while k < len(s3):
            while s1[i] == s3[k]:
                k += 1
                i += 1
                is_exec = True
            if is_exec:
                n += 1
                is_exec = False
                continue
            while s2[j] == s3[k]:
                k += 1
                j += 1
                is_exec = True
            if is_exec:
                m += 1
                is_exec = False
                continue
            break
    return k>=len(s3) and abs(n - m) <= 1


print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))
