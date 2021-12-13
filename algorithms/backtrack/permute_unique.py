"""
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permute_unique(nums):
    perms = [[]]
    for n in nums:
        print("\nn=", n)
        new_perms = []
        for l in perms:
            print("l=", l)
            for i in range(len(l)+1):
                print("i=", i)
                new_perms.append(l[:i]+[n]+l[i:])
                print("new_perms=", new_perms)
                if i < len(l) and l[i] == n:
                    break  # handles duplication
        perms = new_perms
    return perms


nums = [1, 1, 2, 3]
permute_unique(nums)