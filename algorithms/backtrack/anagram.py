"""
Given two strings, determine if they are equal after reordering.

Examples:
"apple", "pleap"  -> True
"apple", "cherry" -> False
"""


def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for c in s1:
        pos = ord(c)-ord('a')
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c)-ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2


def anagram_2(s1, s2):
    s1_list = list(s1)
    s1_list.sort()

    s2_list = list(s2)
    s2_list.sort()

    return s1_list == s2_list


def anagram_3(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2



print(anagram("apple", "pleap"))
print(anagram_2("apple", "pleap"))
print(anagram_3("apple", "pleap"))

print(anagram("apple", "cherry"))
print(anagram_2("apple", "cherry"))
print(anagram_3("apple", "cherry"))
