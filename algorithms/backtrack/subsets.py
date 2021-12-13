"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def subsets(nums):
    """
    O(2**n)
    """
    def backtrack(res, nums, stack, pos):
        print("\nres:", res, "\nnums:", nums, "\nstack:", stack, "\npos:", pos)
        if pos == len(nums):
            res.append(list(stack))
        else:
            # take nums[pos]
            stack.append(nums[pos])
            print("[backtrack 1]")
            backtrack(res, nums, stack, pos+1)
            stack.pop()
            # dont take nums[pos]
            print("[backtrack 2]")
            backtrack(res, nums, stack, pos+1)

    res = []
    backtrack(res, nums, [], 0)
    return res

nums = [1,2,3]
nums = [1, 2, 2]
print(subsets(nums))

"""
simplified backtrack

def backtrack(res, nums, cur, pos):
    if pos >= len(nums):
        res.append(cur)
    else:
        backtrack(res, nums, cur+[nums[pos]], pos+1)
        backtrack(res, nums, cur, pos+1)
"""


# Iteratively
def subsets_v2(nums):
    res = [[]]
    for num in sorted(nums):

        print("res before:", res)
        print("[num]:", [num])

        res += [item+[num] for item in res]

        print("res after:", res, "\n")
    return res

# nums = [1,2,3]
# print(subsets_v2(nums))