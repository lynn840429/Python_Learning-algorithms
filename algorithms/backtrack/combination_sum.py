"""
Given a set of candidate numbers (C) (without duplicates) and a target number
(T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

import time


class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print(self.name)
        print("Elapsed:", (time.time() - self.tstart))


def combination_sum(candidates, target):

    def dfs(nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            dfs(nums=nums, 
                target=(target-nums[i]), 
                index=i, 
                path=(path+[nums[i]]), 
                res=res)

    res = []
    candidates.sort()
    dfs(nums=candidates, target=target, index=0, path=[], res=res)
    return res


candidates, target = [2, 3, 6, 7], 7

with Timer('combination_sum'):
    print(combination_sum(candidates, target))
