import itertools

def get_combinations_with_r(s):
    M = (itertools.groupby(s))
    G = []
    for i in M:
        G.append((len(list(i[1])), int(i[0])))
    return G

if __name__ == "__main__":
    print(get_combinations_with_r('1222311'))
