from math import*


def main(x, z):
    temp = 52
    res = 0
    for i in range(len(x)):
        res = res + cos(58*(z[int(i/2)])**3-(x[i])**2-x[i])
    result = res*temp
    return result
