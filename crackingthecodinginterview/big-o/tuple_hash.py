
import timeit

d = {}
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
d[a] = 10

def func():
    c = d[a]


if __name__ == "__main__":
    print(timeit.timeit('func()', setup="from __main__ import func"))

