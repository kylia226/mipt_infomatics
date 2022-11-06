l = [0, 1, 2, 3, 4, 5]
for i in l:
    if l[1] != i:
        continue
    l[1] += i
print(l)
