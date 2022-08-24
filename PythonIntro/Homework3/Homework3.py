
#Task1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from audioop import reverse
from base64 import b16decode
from calendar import IllegalMonthError
from lib2to3.pgen2.token import NEWLINE


def Task1(l):
    sum = 0
    list1 = [x for x in l if not x%2]
    for elements in list1:
        sum = sum + elements
    return sum

l = [1,2,3,4,5,6]
print(Task1(l))


#Task2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def Task2 (l):
    n = len(l)
    finalList = []
    while n!=0:
       if n>=2:
            finalList.append(l[0]*l[(-1)])
            l.pop(0)
            l.pop(-1)
            n = len(l)
       elif n==1:
            finalList.append(l[0]*l[0])
            break
    
        
    return finalList

l = [1,2,3,4,5,6]
print(Task2(l))

#Task3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import math

def Task3 (l):
    newList = []
    for i in l:
        newList.append(i%1)
    result = max(newList) - min (newList)
    return result

l = [1.1, 1.2, 3.1, 5, 10.01]
print(Task3(l))

#Task4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def Task4(n):
    bin = ""
    while n>0:
        bin = str(n%2)+bin
        n = n//2
    return bin

print(Task4(45))

#Task5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Task5(n):
    list1 = []
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        list1.append(fib2)
    list1.insert(0, 1)
    list1.insert(0, 1)
    list2 = []
    fib3 = 1
    fib4 = -1
    for i in range(2, n):
        fib3, fib4 = fib4, fib3 - fib4
        list2.append(fib4)
    list2.insert(0,-1)
    list2.insert(0,1)
    list2.reverse()
    list3 = list2+[0]+list1
    return list3
    
print(Task5(8))