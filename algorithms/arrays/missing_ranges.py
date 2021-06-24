"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""

def missing_ranges(arr, lo, hi):

    res = []
    start = lo

    for n in arr:

        if n == start:
            start += 1
        elif n > start:
            res.append((start, n-1))
            start = n + 1

    if start <= hi:                 # after done iterating thru array,
        res.append((start, hi))     # append remainder to list

    return res

print(missing_ranges([3, 4], 1, 10))
print(missing_ranges([3, 7], 1, 10))
print(missing_ranges([3, 7], 4, 10))
print(missing_ranges([3, 8], 4, 7))