"""
Swap_pair: A function swap odd and even bits in an integer with as few instructions
as possible (Ex bit and bit 1 are swapped, bit 2 and bit 3 are swapped)

For example:
22: 010110  --> 41: 101001
10: 1010    --> 5 : 0101
"""

"""
We can approach this as operating on the odds bit first, and then the even bits.
We can mask all odd bits with 10101010 in binary ('AA') then shift them right by 1
Similarly, we mask all even bit with 01010101 in binary ('55') then shift them left
by 1. Finally, we merge these two values by OR operation.
"""
import time


def count_time(func):
    def wrapper(arg):
        start = time.time()
        func(arg)
        end = time.time()
        print("Execution Time:%s sec" %(end-start))
    return wrapper


@count_time
def swap_pair(num):
    # odd bit arithmetic right shift 1 bit
    odd = (num & int('AAAAAAAA', 16)) >> 1
    # even bit left shift 1 bit
    even = (num & int('55555555', 16)) << 1

    print(odd | even)
    return odd | even


@count_time
def swap_pair_v2(num):
    num_bin = ''.join(['1' if i=='0'else '0' for i in bin(num)[2:]])
    print(int(num_bin, 2))
    return int(num_bin, 2)



num = 1077
print(swap_pair(num))
print(swap_pair_v2(num))
