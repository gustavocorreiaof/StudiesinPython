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

# with open('file.txt', 'r', encoding='utf-8') as f:
#     conteudo = f.read()
#     print(conteudo)

# import json

# dados = {"name": "João", "age": 30, "city": "São Paulo"}

# with open('date.json', 'w', encoding='utf-8') as f:
#      json.dump(dados, f, ensure_ascii=False, indent=4)

# import json
 
# with open('users.json', 'r', encoding='utf-8') as f:
#     usuarios = json.load(f)
#     for usuario in usuarios:
#         print(f"Name: {usuario['name']}, Age: {usuario['age']}")
        
# dictionarie = [{"Name": "Gustavo", "Age": 25, "City": "Ipaporanga"}, 
#                {"Name": "Alessandro", "Age": 25, "City": "Crateus"}, 
#                {"Name": "Italo", "Age": 18, "City": "Russas"}]

# validAction = True
# options = {"1", "2", "3"}
# option = '1'
# user = 'Miros'

# while(validAction):
#     option = input('Insert a option: 1, 2, 3')

#     if(option in options):
#         validAction = False

# validUser = True

# while(validUser):
#     user = input('Insert a user: "Gustavo", "Alessandro", "Italo"')

#     if(any(user.lower() in person["Name"].lower() for person in dictionarie)):
#         validUser = False

# with open('log.txt', 'w', encoding='utf-8') as f:
#     f.write(f"User: {user} choose the option {option}")

#Advanced Level – Dictionaries, OOP, Errors (36 to 45)========================================================================================================================
# dictionary = [{"Name": "Alessandro", "Age": 26},
#               {"Name": "Alairton", "Age": 23+1},
#               {"Name": "Aligator", "Age": 25},
#               {"Name": "MTT", "Age": 26},
#               {"Name": "Miros", "Age": 25}]

# print(len(dictionary))

# name = 'Alessandro'  # input('Enter the name of the person to search: ')

# has_person_in_dictionary = any(name.lower() in person["Name"].lower() for person in dictionary)

# if has_person_in_dictionary:
#     person = next((v for v in dictionary if v["Name"] == name), None)
#     print(f'There is a person with age {person["Age"]}')
# else:
#     print("There is no such person")

# class BankAccount:
#     def __init__(self, initial_amount):
#         self.balance = float(initial_amount)

#     def deposit(self, amount):
#         self.balance += float(amount)
#         self.show_balance()

#     def withdraw(self, amount):
#         self.balance -= float(amount)
#         self.show_balance()

#     def show_balance(self):
#         print(f'Current account balance: {self.balance}')

# account = BankAccount(100)

# account.show_balance()

# account.deposit(200)

# account.withdraw(25)


# class Pessoa:
#     def __init__(self, nome, idade):
#           self.nome = nome
#           self.idade = idade
    
#     def apresentar(self):
#         print(f"Meu nome é {self.nome}, e tenho idade {self.idade}!")

# class Funcionario(Pessoa):
#      def __init__(self, nome, idade, salario, cargo):
#           super().__init__(nome, idade)
#           self.salario = salario
#           self.cargo = cargo
    
#      def apresentar(self):
#           super().apresentar()
#           print(f'Tenho o cargo de {self.cargo} ganhando {self.salario}')


# funcionario = Funcionario("Gustavo", 25, 1200, "Desenvolvedor")

# funcionario.apresentar()

# try:
#     n1 = 2
#     n2 = 0

#     n3 = n1/n2
# except ZeroDivisionError as e:
#     print(f'Deu erro ai em {e}')

# import os

# agenda = [{"Nome": "Gustavo", "Numero": "88981165549"},
#           {"Nome": "Manel", "Numero": "88888888888"},
#           {"Nome": "Aligator", "Numero": "88981165549"}]

# def funcoes():
#     print('1 - Adicionar')
#     print('2 - Remover')
#     print('3 - Listar')
#     print('4 - Sair')

# def adicionar_contato():
#     nome = input('Digite o nome do contato:  ')
#     numero = input('Digite o numero do contato:  ')

#     agenda.append({"Nome": nome, "Numero": numero})

# def remover():
#     nome = input('Digite o nome do contato que deseja apagar: ')
#     contato_a_remover = next((contato for contato in agenda if contato["Nome"] == nome), None)

#     if contato_a_remover:
#         agenda.remove(contato_a_remover)
#     else:
#         print('Contato inexistente!')

# def listar():
#     for contato in agenda:
#         print(f'Nome do contato: {contato["Nome"]} com o numero: {contato["Numero"]}')

# option = 1;
# while(option != 4):
#     funcoes()
#     option = int(input('Digite uma opção: '))

#     os.system('cls')
#     if option == 1:
#         adicionar_contato()
#     elif option == 2:
#         remover()
#     elif option == 3:
#             listar()
#     else:
#         input('Opção invalida tente novamente')


