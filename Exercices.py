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
