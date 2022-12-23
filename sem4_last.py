# ЗАДАЧА 5.
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях). 

from random import randint
import itertools
import re

k = int(input('Введите степень числа: '))

def Index(k):
    index = [randint(0, 100) 
    for i in range(k + 1)]
    while index[0] == 0:
        index[0] = randint(1, 100) 
    return index

def Multy(k, index):
    var = ['*x^']*(k-1) + ['*x']
    multy = [[a, b, c] for a, b, c  in itertools.zip_longest(index, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in multy:
        x.append(' + ')
    multy = list(itertools.chain(*multy))
    multy[-1] = ' = 0'
    return "".join(map(str, multy)).replace('1*x',' x')

index = Index(k)
multy_1 = Multy(k, index)

k = int(input('Введите степень второго числа: '))

index = Index(k) 
multy_2 = Multy(k, index)

def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol_1 = convert_pol(multy_1)
pol_2 = convert_pol(multy_2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))

print(multy_1)
print(multy_2)
print(pol_sum)