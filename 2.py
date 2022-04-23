from math import*


def main(y):
    if y < 145:
        return 79*y**2+1+28*y**5
    elif y >= 145 and y < 183:
        return (38*y**3)**7
    elif y >= 183 and y < 239:
        return (y**2-y**3)**2
    elif y >= 239:
        return y+95*(sin(63*y**2+54*y+11))**7
