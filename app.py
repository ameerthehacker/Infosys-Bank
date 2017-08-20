from User import User
from Account import Account

def accountMenu():
    choice = -1

    while choice != '4':
        print('\n')
        print('1.SA')
        print('2.CA')
        print('3.FD')
        print('4.Main menu')        
        
        choice = raw_input('Enter your choice: ')

        account_types = { '1': 'SA', '2': 'CA', '3': 'FD' }
        if account_types.has_key(choice):
            if Account.createAccount(5, account_types[choice], 100):
                print 'Account created'
            else:
                print 'Account not created'
        elif choice == '4':
            pass
        else:
            print('Invalid option!')

def userMenu():
    choide = -1

    while choide != '4':
        print('\n')
        print('1.Open New Account')
        print('4.Logout')

        choice = raw_input('Enter your choice: ')

        if choice == '1':
            # show menu for creating a new account
            accountMenu()

        elif choice == '4':
            pass
        else:
            print 'Invalid option!'

def mainMenu():
    choice  = -1    

    while choice != '4':
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
            new_user = User(first_name, last_name, password, address, city, state, pincode)
            if new_user.save():
                print('Thanks for signing up!')
            else:
                print('Cannot create an account for you')
        elif choice == '2':
            attempts = 1
            while attempts <=3:
                print("Attempt %d: "%(attempts))
                id = raw_input('User Id: ')
                password = raw_input('Password: ')
                if User.authenticate(id, password):
                    # show user related menus
                    userMenu()
                    break            
                else:
                    print('Invalid credentials!')
                attempts += 1
            else:
                print('Max sign in attempts reached')
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print('Invalid option!')

# display main menu
accountMenu()

