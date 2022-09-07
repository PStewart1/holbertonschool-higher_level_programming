#!/usr/bin/python3
import sys


if __name__ == "__main__":
    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    if n > 0:
        for i in range(1, n + 1):
            print("{}: {}".format(i, sys.argv[i]))
