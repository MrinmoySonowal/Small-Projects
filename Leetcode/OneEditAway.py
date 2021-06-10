def oneEditReplace(s1: str, s2: str) -> bool:
    found_diff_char = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_diff_char:
                return False
            else:
                found_diff_char = True
    return True


def oneEditInsert(larger_text: str, smaller_text: str) -> bool:
    i = 0
    j = 0
    found_diff_char = False
    while i < len(smaller_text) and j < len(larger_text):
        if larger_text[j] != smaller_text[i]:
            if i != j:
                return False
            else:
                j += 1
                continue
        i += 1
        j += 1
    return True


def is_one_edit_away(s1: str, s2: str) -> bool:
    s1_len, s2_len = len(s1), len(s2)
    if abs(s1_len - s2_len) > 1:
        return False
    elif s1_len == s2_len:
        return oneEditReplace(s1, s2)
    elif s1_len > s2_len:
        return oneEditInsert(s1, s2)
    else:
        return oneEditInsert(s2, s1)


if __name__ == '__main__':
    print(is_one_edit_away("paincccccc", "vain"))
    print(is_one_edit_away("pain", "vain"))
    print(is_one_edit_away("pain", "pin"))
    print(is_one_edit_away("pan", "pain"))
    print(is_one_edit_away("van", "pain"))
