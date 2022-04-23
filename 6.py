def main(x):
    if x[3] == 2007:
        if x[0] == 1992:
            return {'REXX': 0, 'DART': 1}[x[1]]
        elif x[0] == 1958:
            return 2
    elif x[3] == 2017:
        return {'REXX': 3, 'DART': 4}[x[1]]
    elif x[3] == 1999:
        if x[0] == 1992:
            return {'TXL': 5, 'STON': 6, 'CIRRU': 7}[x[2]]
        elif x[0] == 1958:
            return {'REXX': 8, 'DART': 9}[x[1]]
