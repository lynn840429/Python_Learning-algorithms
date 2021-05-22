"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable


# return list
def flatten(input_arr, output_arr=None):
    print("input_arr=", input_arr)
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        print("ele=", ele)
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            print("in if not=", ele)
            flatten(ele, output_arr)    #tail-recursion
        else:
            output_arr.append(ele)      #produce the result
            print("output_arr", output_arr)
    return output_arr


# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)    
        else:
            yield element

print(flatten([1, 2, 3, [4, 5, 6], 7, [8, 9]]))
