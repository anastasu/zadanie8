from itertools import permutations
p = list(permutations('ТЬЮРИНГ'))
k = 0
for a in p:
    a1 = "".join(a)
    if not('ЮЬ' in a1) and not('ИЬ' in a1) and a1[0] != 'Ь' :
        print(a)
        k += 1
print(k)