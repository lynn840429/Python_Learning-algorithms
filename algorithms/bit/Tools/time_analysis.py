# =====================================
# FileName: time_analysis.py
# Usage: @count_time
#        def function():
# Description: Add before functions.
# Dependency: os, sys, time
# Author: Lynn <lynn840429@gmail.com>
# Version: v1.0.0
# =====================================
""" Import Packages """
import os
import sys
import time



""" Function """
def execution_time_no_arg(func):
    """
    Function Info: Function without parameter.
    """
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Execution Time:%s sec" %(end_time-start_time))
    return wrapper


def execution_time_single_arg(func):
    """
    Function Info: Function with one parameter.
    """
    def wrapper(arg):
        start_time = time.time()
        func(arg)
        end_time = time.time()
        print("Execution Time:%s sec" %(end_time-start_time))
    return wrapper


def execution_time_multiple_args(func):
    """
    Function Info: Function with multiple parameters.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(args, kwargs)
        end_time = time.time()
        print("Execution Time:%s sec" %(end_time-start_time))
    return wrapper
