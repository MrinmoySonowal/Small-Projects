from collections import Counter


def is_palindrome(s: str) -> bool:
    """
    O(1) space and O(N) time algorithm to check if a string is a palindrome
    :param s: String in consideration
    :return: True if string is a palindrome string else false
    """
    s = s.lower()
    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def is_permutation_of_palindrome(s: str) -> bool:
    s = s.lower()
    character_count = Counter(s)
    del character_count[' ']
    found_one_odd = False
    for count in character_count.values():
        if (count % 2) != 0 and found_one_odd:
            return False
        elif (count % 2) != 0:
            found_one_odd = True
    return True


if __name__ == '__main__':
    print(is_palindrome("Aba"))
    print(is_permutation_of_palindrome("Tact Coa"))
