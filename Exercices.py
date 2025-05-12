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

# import json

# usuarios = []

# def carrega_usuarios():
#     global usuarios
#     with open('login.json', 'r', encoding='utf-8') as f:
#         usuarios = json.load(f)

# def mostra():
#     for usuario in usuarios:
#         print(f'Usuario-> {usuario["Login"]}, senha -> {usuario["Senha"]}')

# carrega_usuarios()
# mostra()

# import random

# lista = ["Alerrandro", "Ronaldinho", "Bilbo", "Frodo", "Gandalf"]

# print(f'O nome sorteado é:  {random.choice(lista)}')

# import string
# import random

# letras = string.ascii_letters
# numeros = string.digits
# simbolos = string.punctuation

# todos_os_caracteres =  letras + numeros + simbolos

# tamanho_da_senha = random.randrange(8, 12)

# senha = ''.join(random.choice(todos_os_caracteres) for _ in range(tamanho_da_senha))

# print('Senha gerada: ' + senha)

# import requests 

# url = "https://official-joke-api.appspot.com/random_joke"

# response = requests.get(url)

# if response.status_code == 200:
#     piada = response.json()
#     print("Aqui vai uma piada:")
#     print(piada['setup'])   # Começo da piada
#     print(piada['punchline'])  # Final engraçado
# else:
#     print("Erro ao buscar piada:", response.status_code)

import csv

# with open('nomes.txt', 'r', encoding='utf-8') as txt_file:
#     nomes = [linha.strip() for linha in txt_file]

# with open('nomes.csv', 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['Nome'])  
#     for nome in nomes:
#         writer.writerow([nome])

# print("Conversão concluída!")


# with open('vendas.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file) #cria como se fosse um array de linhas
#     next(reader) #pula a primeira linha ou o cabeçalho

#     valor = 0

#     for row in reader: #para cada linha do array
#         valor += float(row[1])

#     print(f'Valor vendido: {valor}')

import matplotlib.pyplot as plt
from datetime import datetime

tarefas_concluidas = {
    '2025-04-25': 5,
    '2025-04-26': 8,
    '2025-04-27': 6,
    '2025-04-28': 10,
    '2025-04-29': 7,
}

datas = [datetime.strptime(data, '%Y-%m-%d') for data in tarefas_concluidas.keys()]
quantidades = list(tarefas_concluidas.values())

# Cria uma nova figura com tamanho 10x5 polegadas
plt.figure(figsize=(10, 5))

# Plota os dados com:
# - datas no eixo x
# - quantidades no eixo y
# - 'o' para marcar os pontos
# - linha contínua '-'
# - cor azul
plt.plot(datas, quantidades, marker='o', linestyle='-', color='purple')

# Define o título do gráfico
plt.title('Tarefas Concluídas por Dia')

# Define o rótulo (label) do eixo X
plt.xlabel('Data')

# Define o rótulo (label) do eixo Y
plt.ylabel('Quantidade de Tarefas')

# Adiciona uma grade ao fundo do gráfico para facilitar a leitura
plt.grid(True)

# Rotaciona os rótulos das datas no eixo X para 45 graus (melhora a legibilidade)
plt.xticks(rotation=45)

# Ajusta automaticamente o layout para evitar sobreposição dos elementos
plt.tight_layout()

# Exibe o gráfico na tela
plt.show()

import json
import os

ARQUIVO = 'usuarios.json'


def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        return json.load(f)


def salvar_usuarios(usuarios):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)


def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    idade = input("Idade: ")

    usuarios = carregar_usuarios()


    if any(user['email'] == email for user in usuarios):
        print("Usuário com esse email já existe.")
        return

    usuarios.append({'nome': nome, 'email': email, 'idade': idade})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, user in enumerate(usuarios, start=1):
            print(f"{i}. {user['nome']} - {user['email']} - {user['idade']} anos")


def buscar_usuario():
    email = input("Digite o email do usuário: ")
    usuarios = carregar_usuarios()
    for user in usuarios:
        if user['email'] == email:
            print(f"Nome: {user['nome']}, Idade: {user['idade']}")
            return
    print("Usuário não encontrado.")

def remover_usuario():
    email = input("Digite o email do usuário a remover: ")
    usuarios = carregar_usuarios()
    novos_usuarios = [user for user in usuarios if user['email'] != email]

    if len(novos_usuarios) == len(usuarios):
        print("Usuário não encontrado.")
    else:
        salvar_usuarios(novos_usuarios)
        print("Usuário removido com sucesso.")

def menu():
    while True:
        print("\n--- Sistema de Cadastro ---")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário por email")
        print("4. Remover usuário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            remover_usuario()
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" não está disponível.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro "{self.titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.titulo}" já está disponível.')

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f'"{self.titulo}" por {self.autor} - {status}'


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca.')

    def listar_livros(self):
        print("\n📚 Lista de livros na biblioteca:")
        for livro in self.livros:
            print(f"- {livro}")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                livro.emprestar()
                return
        print(f'Livro "{titulo}" não encontrado.')

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                livro.devolver()
                return
        print(f'Livro "{titulo}" não encontrado.')

if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.listar_livros()

    biblioteca.emprestar_livro("1984")
    biblioteca.listar_livros()

    biblioteca.devolver_livro("1984")
    biblioteca.listar_livros()

