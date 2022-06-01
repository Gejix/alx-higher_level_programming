#!/usr/bin/python3
for n in range(97, 123):
    if (n == 101 or n == 113):
        print(end="")
    else:
        print("{}".format(chr(n)), end="")
