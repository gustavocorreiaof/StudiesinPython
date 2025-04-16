import os

restaurants = ["Casa Blanca", "Karatiuis", "InovaFit"]

def finish_app():
    os.system('cls')
    print('Exit')
    input('Enter any key to return main menu.\n')
    main()

def register_Restaurant():
    os.system('cls')
    new_restaurant = input('Enter the name of new restaurant:  ')
    restaurants.append(new_restaurants)
    input('Enter any key to return main menu.\n')
    main()

def main():
    try:
        os.system('cls')
        print('Taste Express')
        print('1. Register restaurant.')
        print('2. List restaurants.')
        print('3. Activate restaurant.')
        print('4. Exit')

        option = int(input('Choose an option: '))
        if option == 1:
            register_Restaurant()
        elif option == 2:
            list_restaurants()
        elif option == 3:
            print('Activate Restaurant')
        else:
            finish_app()
    except:
        print('Invalid option!')

def list_restaurants():
    i = 1
    for restaurant in restaurants:
        print(f'{i}. {restaurant}')
        i= i + 1;
    
    input('Enter any key to return main menu.\n')
    main()

main()

