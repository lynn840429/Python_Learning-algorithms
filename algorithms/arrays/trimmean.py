"""
When make reliable means, we need to neglect best and worst values.
For example, when making average score on athletes we need this option.
So, this algorithm affixes some percentage to neglect when making mean.
For example, if you suggest 20%, it will neglect the best 10% of values
and the worst 10% of values.

This algorithm takes an array and percentage to neglect. After sorted,
if index of array is larger or smaller than desired ratio, we don't
compute it.

Compleity: O(n)
"""
import statistics

def trimmean(arr, per):
    ratio = per/200
    # /100 for easy calculation by *, and /2 for easy adaption to best and worst parts.
    cal_sum = 0
    # sum value to be calculated to trimmean.
    arr.sort()
    neg_val = int(len(arr)*ratio)
    arr = arr[neg_val:len(arr)-neg_val]

    print("m1_val=", statistics.mean(arr))
    print("m2_val=", sum(arr) / len(arr))

    for i in arr:
        cal_sum += i
    return cal_sum/len(arr)

arr = [1, 1, 1, 3, 7, 9, 4, 3, 5, 46, 12, 4111, 875, 123, 45, 56, 89, 34, 59, 10]
per = 10
print(trimmean(arr, per))