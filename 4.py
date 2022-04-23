from math import*


def main(n):
    if n == 0:
        return 0.63
    elif n == 1:
        return -0.91
    elif n >= 2:
        return 1-(main(n-2))**3-(main(n-1))**2
