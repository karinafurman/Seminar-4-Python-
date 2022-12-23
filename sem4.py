ЗАДАЧА 1
Вычислить число c заданной точностью d

d = (float(input("Задайте искомую точность: ")))
count = 0
n = str(3.141592653589793238462643383279502884197169399375105820974944)
while d < 0:
    d *= 10
    count += 1
print(str(n.split('.')[1][count]))



ЗАДАЧА 2
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число: '))

count = 2
multipliers = []
while count * count <= N:
    while N % count == 0:
        multipliers.append(count)
        N = N / count
    count += 1
if N > 1:
    multipliers.append(N) 
print(multipliers)



ЗАДАЧА 3
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3] -- удалить повторки полностью не получилось, код выводит только список уникальных элементов

input_list = [1, 1, 2, 3, 4, 4, 4]
output_list = []
[output_list.append(i) for i in input_list if i not in output_list]
print(output_list)


ЗАДАЧА 4.
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.


from random import randint
import itertools

k = int(input('Введите степень '))

def get_ratios(k):
    ratios = [randint(0, 100) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 100) 
    return ratios
print(get_ratios(k))

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace('1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)


