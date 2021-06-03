"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

Complexity = O(n)
"""
import time

# tl:dr -- array slicing by value
## M1
def limit(arr, min_lim=None, max_lim=None):
    min_check = lambda val: True if min_lim is None else (min_lim <= val)
    max_check = lambda val: True if max_lim is None else (val <= max_lim)
    
    return [val for val in arr if min_check(val) and max_check(val)]

time1 = time.time()
print(limit([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
time2 = time.time()
print('{:s} function took {:.3f} ms'.format("limit", (time2-time1)*1000.0))


## M2
def limit2(arr, min_lim=None, max_lim=None):
    sort_arr = sorted(arr)
    if (min_lim==None):  min_lim = sort_arr[0]
    if (max_lim==None): max_lim = sort_arr[-1]
    return [val for val in arr if val<=max_lim and val>=min_lim]

time1 = time.time()
print(limit2([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
time2 = time.time()
print('{:s} function took {:.3f} ms'.format("limit2", (time2-time1)*1000.0))
