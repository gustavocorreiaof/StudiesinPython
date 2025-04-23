# # Beginner Level – Fundamentals (1 to 10) ==============================================================================================================================================================================================

# #--1
# print('Hello world!')

# #--2
# name = input('Enter your name: ')
# print(f'Hello {name}')

# #--3
# number_1 = int(input('Enter a number: '))
# number_2 = int(input('Enter another number: '))
# print(f'Sum of both numbers: {number_1 + number_2}')

# #--4
# n_1 = int(input('Enter a number: '))
# n_2 = int(input('Enter another number: '))
# n_3 = int(input('Enter the last number: '))
# print(f'The average of the numbers is: {(n_1 + n_2 + n_3) / 3}')

# #--5
# number = int(input('Enter a number: '))
# print("Even number" if number % 2 == 0 else "Odd number")

# #--6
# for num in range(1, 51):
#     if num % 2 == 0:
#         print(num)

# #--7
# num = int(input('Enter a number: '))
# print('Positive number!' if num > 0 else 'Negative number')

# #--10
# tab = int(input('Enter a number: '))
# print(f'Times table of number {tab}:')

# for num in range(1, 11):
#     print(f'\nNumber: {tab * num}')

# Beginner Level – Flow Control and Lists (11 to 20) ==============================================================================================================================================================================================

# i = 1

# while(i <=100):
#     print(i)
#     i+=1;

# for num in range(1, 101):
#     print(num)

# lista = []

# lista = input('Enter 5 numbers separated by spaces:  ').split()
# lista = [int(num) for num in lista]

# print(f'Entered numbers: {lista}')

# even_count = sum(1 for num in lista if num % 2 == 0)

# print(f'Even numbers: {even_count}')


# word = input('Enter a word:  ')

# for c in word:
#     print(c)

# print('Word in reverse:  ' + word[::-1])

# Intermediate Level – Functions, Modules, and Files (21 to 35) ===============================================================================================================================================================================================

# import math

# def factorial(n):
#     print(f'The factorial of {n} is: {math.factorial(n)}')

# n = int(input('Enter the number you want to know the factorial of:  '))

# factorial(n)


# my_set = {1, 2, 3, 3}

# print(my_set)
# print(f"My set count: {len(my_set)}")


# numbers_list = input('Enter a list of numbers separated by spaces: ').split()
# numbers_list = list(map(int, numbers_list))
# sum_of_numbers = sum(numbers_list)

# print(f'The average of these numbers is {sum_of_numbers / len(numbers_list)}')

# print(f'Max number in the list: {max(numbers_list)}')
# print(f'Min number in the list: {min(numbers_list)}')

# sentence = input('Enter a sentence: ')

# vowels = ('a', 'e', 'i', 'o', 'u')

# count = 0

# for char in sentence:
#     if char in vowels:
#         count += 1

# print(f'The sentence contains: {count} vowels!')

# how_many = int(input('Enter how many names you want to save: '))

# names = []

# for n in range(how_many):
#     names.append(input('Enter a name: '))

# with open('names.txt', 'w', encoding='utf-8') as file:
#     for name in names:
#         file.write(name + '\n')

with open('file.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print(conteudo)

import json

dados = {"name": "João", "age": 30, "city": "São Paulo"}

with open('date.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

import json

with open('users.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)
    for usuario in usuarios:
        print(f"Name: {usuario['name']}, Age: {usuario['age']}")
        