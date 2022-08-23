
#Task 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def Task1(a):
    summary = 0
    number = int(str(a).replace(".",""))
    while number > 0:
         b = number % 10
         summary = summary + b
         number = number // 10
    return summary;

print(Task1(1.2345))


#Task 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def Task2(n):
    product = 1
    for i in range(1,n+1):
        product *= i;
    return product

print(Task2(5))

#Task 3. Реализуйте алгоритм перемешивания списка.
import random
def Task3(l):
    for i in range(0,len(l)-1):
        k = random.randint(0, len(l) - 1)
        l[i],l[k] = l[k],l[i]
    return l;

print(Task3([20,33,50,111,215,152]))