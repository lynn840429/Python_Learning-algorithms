"""
Given a digit string, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below:
2: "abc"
3: "def"
4: "ghi"
5: "jkl"
6: "mno"
7: "pqrs"
8: "tuv"
9: "wxyz"

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
import time
import itertools

def letter_combinations(digits):
    if digits == "":
        return []
    kmaps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    ans = [""]
    for num in digits:
        tmp = []
        for an in ans:
            for char in kmaps[num]:
                tmp.append(an + char)
        ans = tmp
    return ans

start_time = time.time()
print(letter_combinations("3579"))
print("--- %s seconds ---" % (time.time() - start_time))

#----------------------------------------
def letter_combinations_v2(digits):
    if digits == "":
        return []
    kmaps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    elements = [kmaps[i] for i in digits]
    return [''.join(ele) for ele in list(itertools.product(*elements))]
    
start_time = time.time()
print(letter_combinations_v2("3579"))
print("--- %s seconds ---" % (time.time() - start_time))