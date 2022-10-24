def print_map(function, iterable):
    iterator = iter(iterable)
    i = 0
    while i < len(iterable):
        i += 1
        print(function(next(iterator)))

def function(i):
    return i ** 2

iterable = [1, 2, 3, 4, 5, 6]
print(print_map(function, iterable))
