"""
Remove_bit(num, i): remove a bit at specific position.
For example:

Input: num = 10101 (21)
remove_bit(num, 2): output = 1001 (9)
remove_bit(num, 4): output = 101 (5)
remove_bit(num, 0): output = 1010 (10)
"""

def remove_bit(num, i):
    print(num, "=", bin(num)[2:])

    mask = num >> (i + 1)
    print("mask =", bin(mask)[2:])

    mask = mask << i
    print("mask =", bin(mask)[2:])

    right = ((1 << i) - 1) & num
    print("right =", bin(right)[2:])

    print("Ans =", bin(mask | right)[2:])

    return mask | right

num, i = 21, 4
print(remove_bit(num, i))
