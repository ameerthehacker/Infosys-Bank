from User import User

def mainMenu():
    choice  = -1    

    while choice != 4:
        print('\n')
        print('1.Sign Up')
        print('2.Sign In')
        print('3.Admin Sign In')
        print('4.Quit')

        choice = raw_input('Enter your choice: ')

        if choice == '1':
            first_name = raw_input('First Name: ')
            last_name = raw_input('Last Name: ')
            password = raw_input('Password: ')            
            address = raw_input('Address: ')
            city = raw_input('City: ')
            state = raw_input('State: ')
            pincode = raw_input('Pincode: ')
            account_type = input('Enter your choice: ')
            new_user = User(first_name, last_name, password, address, city, state, pincode)
            if new_user.save():
                print('Thanks for signing up!')
            else:
                print('Cannot create an account for you')
        elif choice == '2':
            password
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print('Invalid option!')

# display main menu
mainMenu()

