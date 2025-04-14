import os

print('Taste Express')
print('1. Register restaurant.')
print('2. List restaurants.')
print('3. Activate restaurant.')
print('4. Exit')

option = int(input('Choose an option: ')  )

def finish_app():
    os.system('cls')
    print('Exit')

if option == 1:
    print('Register restaurant')
elif option == 2:
    print('List Restaurant')
elif option == 3:
    print('Activate Restaurant')
else:
    finish_app();