from math import log10


def main(x, y, z):
    res = 0
    for k in range(1, y+1):
        temp1 = 1-k**3
        for i in range(1, x+1):
            res += (temp1-62*i)**2+20*((log10(i))**3)+26
    for c in range(1, x+1):
        temp1 = c**2
        temp2 = temp1**3
        for j in range(1, z+1):
            res += temp1+j+temp2
    return res
