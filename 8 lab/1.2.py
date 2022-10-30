import itertools

def get_cartesian_product(a, b):
    return itertools.product(a,b)
  
print(list(get_cartesian_product([34, 22], [1, 46])))
