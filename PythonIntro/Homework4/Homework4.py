#Task1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 

def Task1 (N):
    list1= []
    d = 2
    while N>1:
        while N%d == 0:
            list1.append(d)
            N//= d
        d += 1
    return list1
print("Задание № 1.")
while True:
    try:
        n = int(input('Задайте натуральное число N: '))
        print(Task1(n))
        break
    except:
        print("Неверный формат ввода. Повторите попытку.")

#Task2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.
def Task2 (list1):
    uniqueNumbers = []
    for number in list1:
        if number not in uniqueNumbers:
            uniqueNumbers.append(number)
    return uniqueNumbers

print("Задание № 2.")
while True:
    try:
        list1 = list(map(int,input('Задайте последовательность чисел: ').split()))
        print(Task2(list1))
        break
    except:
        print("Неверный формат ввода. Повторите попытку.")



#Task3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.

import random

    

def Task3 (k):
    result = ""
    
    while k > 0:
        if k == 1:
                 result += f'{random.randint(0, 100)} * x + '
        else:
            result += f'{random.randint(0, 100)} * x^{k} + '
        k -= 1

    else:
        while k < 0:
            result += f'{random.randint(0, 100)} * x^{k} + '
            k += 1
    result += f'{random.randint(0, 100)} = 0'
    
    with open("homework4.txt",'+a') as f:
        f.write(result + '\n')
    
    return result

print("Задание № 3.")
while True:
    try:
        k = int(input('Введите коэффициент степени для многочлена: '))
        print(Task3(k))
        break
    except:
        print("Неверный формат ввода. Повторите попытку.")
    
    
    