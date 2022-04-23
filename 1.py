from math import*


def main(x, z):
    a = 18-7*(tan(1-38*z**3-78*x**2))**2
    b = 40*x**3-32*z**5
    c = x**12
    d = acos(z)/24
    result = (a/b)+c-d
    return result
