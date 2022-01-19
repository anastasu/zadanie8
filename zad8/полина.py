from itertools import product
p = list(product('01234', repeat=5))
k = 0
for a in p:
    if a[0] != '0' and (a.count('0') + a.count('2') + a.count('4') <= 3):
        k += 1
print(k)   