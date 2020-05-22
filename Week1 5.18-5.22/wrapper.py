import logging
import time

def print_run_time(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(*args, **kwargs)
        end = time.clock()
        print("{} run time {}".format(func.__name__, end-start))
    return wrapper


@print_run_time
def foo(name='foo'):
    print("i am %s" % name)
    print('----')
    for i in range(10000000):
        pass
foo()