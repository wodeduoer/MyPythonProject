# file TimerSeq.py

import sys
import time

req = 1000
size = 10000


def test_time(func, *args):
    start_time = time.time()
    for i in range(req):
        func(*args)
    elapse = time.time() - start_time
    return elapse


def for_statement():
    res = []
    for x in range(size):
        res.append(abs(x))


def list_comprehension():
    res = [abs(x) for x in range(size)]


def map_statement():
    res = map(abs, range(size))


def generator_statement():
    res = list(abs(x) for x in range(size))


print(sys.version)
test_func = (for_statement, list_comprehension, map_statement, generator_statement)
for test in test_func:
    print(test.__name__.ljust(20), '=====>', test_time(test))

