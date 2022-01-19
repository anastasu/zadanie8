from itertools import product
p = list(product('01234567', repeat=4))
k = 0
for a in p:
    if a[0] != '0' and int(' '.join(a), 8) % 4 == 0:
         k += 1
print(k)
