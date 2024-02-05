from time import time, sleep

# -*- coding: utf-8 -*-
def another_function(func):
    start = time()

    def other_func():
        return time()-start
    return other_func


@another_function
def a_function():
    sleep(2)
    return 456**25


if __name__ == "__main__":
    value = a_function()
    print(value)