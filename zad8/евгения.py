from itertools import product
p = list(product('01234567', repeat=4))
k = 0
for a in p:
    if a[0] != '0' and a[0] in ('2', '4', '6') and a[0] >= a[1] >= a[2]>= a[3] :
        k += 1
print(k)