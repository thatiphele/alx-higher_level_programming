#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    x = (len(sys.argv)) + (-1)
    if x == 1:
        print("1 argument: ")
    elif x == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(x))
    for y in range(x):
        print("{}: {}".format(y + 1, sys.argv[y + 1]))