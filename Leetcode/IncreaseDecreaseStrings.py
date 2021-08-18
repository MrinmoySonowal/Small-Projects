from collections import Counter


def sortString(s: str) -> str:
    ctr_word = Counter(s)
    sorted_keys = sorted(ctr_word.keys())
    rev_flag = False
    res = ""
    while len(res) != len(s):
        if rev_flag:
            for ch in sorted_keys[::-1]:
                if ctr_word[ch] == 0:
                    del ctr_word[ch]
                    continue
                res += ch
                ctr_word[ch] -= 1
            rev_flag = False
        else:
            for ch in sorted_keys:
                if ctr_word[ch] == 0:
                    del ctr_word[ch]
                    continue
                res += ch
                ctr_word[ch] -= 1
            rev_flag = True
    return res


if __name__ == '__main__':
    print(sortString("abbabbaccc"))
