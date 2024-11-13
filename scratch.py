# list1 = [0,1]
# def fibonacci(n):
#     if len(list1) == n:
#         return list1[n-1]
#     list1.append(list1[-1] + list1[-2])
#     return
# input()
# print(fibonacci(6))  # Вывод: 8 (последовательность: 0, 1, 1, 2, 3, 5, 8)
import math
# list1 = [0, 1]
# list2 = [list1[1], list1[0] + list1[1]]
# list1 = [0, 1]
# while len(set(list1)) != 6:
#     list1.append(list1[-1] + list1[-2])
# print(list1[-1])



# def recursive_sum(n):
#     if n == 0:
#         return 0
#     return n + recursive_sum(n-1)
#
# print(recursive_sum(5))

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(5))  # Вывод: 120 (5! = 5 * 4 * 3 * 2 * 1)

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Пример использования
# print(fibonacci(6))  # Вывод: 8

# def reverse_string(s):
#     if len(s) == 0:
#         return ''
#     return s[-1] + reverse_string(s[:-1])
# print(reverse_string("hello"))  # Вывод: "olleh"

# def rec1 (n):
#     if n == 1:
#         return 1
#     return n + rec1(n - 1)
#
# print(rec1(6))

# def rec2 (n):
#     if n == 0:
#         return 1
#     return n * rec2(n-1)
#
# print(rec2(6))

# def rec3(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return rec3(n-1) + rec3(n-2)
#
# print(rec3(6))

# def rec4(n):
#     if n  == 0:
#         return True
#     elif n == 1:
#         return False
#     else:
#         return rec4(n-2)
#
# print(rec4(5))

# def rec5(n):
#     if len(n) == 0:
#         return ''
#     else:
#         return n[-1] + rec5(n[:-1])
#
# print(rec5('Hello'))


# def rec6(n):
#     a = 0
#     if len(str(n)) == 1:
#         return 1
#     else:
#         return a + 1 + rec6(n//10)
#
# print(rec6(123))

# def rec7(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         return rec7(n-1)
#
# rec7(3)

# def rec8(n, a = 2):
#     if n % a == 0:
#         print(a)
#     return rec8(n, a+1)
#
# print(rec8(8))

# def rec9(list1):
#     if len(list1) == 1:
#         return list1[0]
#     else:
#         a = rec9(list1[1:])
#         return list1[0] if list1[0] < a else a
#
# list2 = [1,2,3]
# print(rec9(list2))
# list2.remove(list2[1])
# print(list2)

# def rec10(n):
#     b = []
#     if ...:
#         ...
#     else:
#         for i in n:
#             for j in n[1:]
#                 b = [i] + shuffle(n[1:])
#     print(b)
#
#
# print(rec10([1,2,3]))

# def log_function(func):
#     def inner(x,y):
#         print(f'Function {func.__name__}, arguments {(x,y)}')
#     return inner
#
# @log_function
# def add(a, b):
#     return a + b
# add(3, 5)  # Вывод: Вызов функции add с аргументами (3, 5)

# import time
#
# def timeit(func):
#     def inner():
#         a = time.time()
#         func()
#         print(f'Time: {time.time() - a}')
#     return inner
#
#
# @timeit
# def slow_function():
#     time.sleep(2)
# slow_function()  # Вывод: Затраченное время: 2.0 сек.

import os
import string
import time
from posixpath import split
from tokenize import blank_re


# 1


# file = 'text_example.txt'
# if os.path.exists(file):
#     with open(file, 'a+') as file:
#         file.seek(0)
#         list1 = file.readline().split(', ')
#         print(list1)
# else:
#     with open(file, 'w') as file:
#         list1 = []
#         while True:
#             a = int(input('''0 - Save to file
# 1 - Add user name\n'''))
#             if a == 1:
#                 a = input('Enter username: ')
#                 list1.append(a)
#                 # file.write(a)
#             elif a == 0:
#                 break
#         file.write(', '.join(list1) + '.')


# 2

# def recnum(n):
#     if n == 0:
#         return 0
#     return n % 10 + recnum(n//10)
# print(recnum(285))


# 3


# file = 'text_example.txt'
# a = 0
# b = 0
# list1 = []
# with open(file, 'r+') as file:
#     for i in file:
#         b += 1
#         if i.count('Python') !=0 or i.count('python') !=0:
#             a += i.count('Python')
#             a += i.count('python')
#             list1.append(b)
#     print(a)
#     print(list1)
#
# with open ('text_example.txt', 'r') as f:
#   old_data1 = f.read()
#
# new_data1 = old_data1.replace('Python', 'Machine learning')
#
#
# with open ('text_example.txt', 'w') as f:
#   f.write(new_data1)
#
# with open('text_example.txt', 'r') as f:
#     old_data2 = f.read()
#
# new_data2 = old_data2.replace('python', 'machine learning')
#
# with open ('text_example.txt', 'w') as f:
#   f.write(new_data2)
# 4

# def listchange(n):
#     b = 0
#     for i in range(len(n) - 1):
#         if n[i] > n[i+1]:
#             b += (n[i] - n[i+1]) + 1
#             n[i + 1] += b
#     return b
# a =  [-10, 0, -2, 0]
# print(listchange(a))

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print(fib(7))

# def powab(a,b):
#     if b == 0:
#         return 1
#     return a * powab(a, b-1)
#
# print(powab(5,3))

# def aut(func):
#     def inner():
#         a = input('Enter pasword: ')
#         if a == 'qwerty':
#             func()
#         else:
#             print('Uncorrect pasword')
#     return inner
#
#
# @aut
# def welcome():
#     print('Hi, welcome my friend')
#
# welcome()

# with open('text_example.txt', 'r') as f:
#     for i in a:
#         for j in i:


# with open('text_example.txt', 'w') as f:
#     b = sorted((lambda x: letter for letter in a.split() if letter.isalpha()))
#
# print(b)

# 1

# def greenDec(func):
#     def inner():
#         print('\033[92m')
#         func()
#         print('\033[0m')
#     return inner
#
# def redDec(func):
#     def inner():
#         print('\033[31m')
#         func()
#         print('\033[0m')
#     return inner
#
# def blueDec(func):
#     def inner():
#         print('\033[34m')
#         func()
#         print('\033[0m')
#     return inner
#
# @redDec
# def decorteIt():
#     print('Hello')
# decorteIt()

# 2

# def logAB(func):
#     def inner(x,y):
#         func = math.log(x,y)
#         return func
#     return inner
#
#
# @logAB
# def calculateAB(a,b):
#     return a-b
#
# print(calculateAB(8,2))

# 3

# d1 = {}
#
# def decfib(func):
#     def inner(x):
#         if x in d1:
#             print('The result was found for the current values')
#             return d1[x]
#         else:
#             a = func(x)
#             d1[x] = a
#             print(d1)
#             return a
#     return inner
#
#
# @decfib
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)
# input()
# print(fib(6))
# b = [i for i in range(10000000)]
# my_set = set(b)
# a = time.time()
# print(3 in my_set)
# c = time.time()
# print(3 in b)
# print(c - a == time.time() - c)
# import faker
# f = faker.Faker(locale='ru_RU' )
# for i in range(10):
#     print(f.first_name(),f.last_name(), f.date(), f.country(), f.city(), f.color(), f.job())
import time


timeNow = time.time()
locTime = time.localtime(timeNow)
timeHour = locTime.tm_hour


def dec(func):
    def inner(v):
        if timeHour > 10 and timeHour < 19:
            func(v)
        else:
            print("Sorry, it's too late.")
    return inner


@dec
def f(a):
    print(f'Welcome {a}!')
    return 0

f('Варужан')
