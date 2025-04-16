import os

restaurants = ["Casa Blanca", "Karatiuis", "InovaFit"]

main()

def finish_app():
    os.system('cls')
    print('Exit')

def register_Restaurant():
    os.system('cls')
    new_restaurant = input('Enter the name of new restaurant:  ')
    restaurants.append(new_restaurants)
    main()

def main():
    print('Taste Express')
    print('1. Register restaurant.')
    print('2. List restaurants.')
    print('3. Activate restaurant.')
    print('4. Exit')

    option = int(input('Choose an option: '))
    if option == 1:
        register_Restaurant()
    elif option == 2:
        print('List Restaurant')
    elif option == 3:
        print('Activate Restaurant')
    else:
        finish_app()