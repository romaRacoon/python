def main(x):
    if x[0] == 'SELF':
        if x[3] == 1980:
            if x[1] == 2015:
                return {1976: 2, 1961: 3}[x[4]]
            return {1978: 0, 1994: 1}[x[1]]
        elif x[3] == 1963:
            if x[4] == 1976:
                return {1978: 4, 1994: 5, 2015: 6}[x[1]]
            return 7
    elif x[0] == 'FREGE':
        if x[4] == 1976:
            if x[2] == 'RAGEL':
                return {1978: 8, 1994: 9, 2015: 10}[x[1]]
            return {'XTEND': 11, 'HCL': 12}[x[2]]
        return 13
