import itertools

def get_combinations_with_r(s, n):
    M = sorted(itertools.combinations_with_replacement(s,n))
    for i in range(len(M)):
        M[i] = "".join(sorted(list(M[i])))
    return M
  
  
if __name__ == "__main__":
    print(get_combinations_with_r("cat", 2))
