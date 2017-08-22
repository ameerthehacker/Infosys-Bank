from User import User
from Database import Database as db
from Account import Account
from SAccount import SAccount
from CAccount import CAccount
from Admin import Admin

def getAccountObj(id):
    if Account.accountExist(id):
        account = Account(id)
        if account.type == 'CA':
            account = CAccount(id)
        elif account.type == 'SA':
            account = SAccount(id)
        return account
    else:
        return 0

def accountMenu(current_user):
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
            account_type = account_types[choice]
            if(account_type == 'SA'):
                SAccount.createAccount(current_user)
            elif(account_type == 'CA'):
                CAccount.createAccount(current_user)                

            print('Account created!')
        elif choice == '4':
            pass
        else:
            print('Invalid option!')

def userMenu(current_user):
    choice = -1

    while choice != '7':
        print('\n')
        print('1.Open New Account')
        print('2.Change Address')
        print('3.Deposit Amount')  
        print('4.Withdraw Amount')                      
        print('5.Print Statement')                              
        print('6.Close Account')                              
        print('7.Logout')

        choice = raw_input('Enter your choice: ')

        if choice == '1':
            # show menu for creating a new account
            accountMenu(current_user)
        if choice == '2':
            address = raw_input('Address: ')
            city = raw_input('City: ')
            state = raw_input('State: ')
            pincode = raw_input('Pincode: ')
            query = "UPDATE users SET address = %s, city = %s, state = %s, pincode = %s"
            cur = db.getCursor()
            if cur.execute(query, (address, city, state, pincode)):
                db.commit()
                print('Address was updated!')
            else:
                print('Address could not be updated')
        if choice == '3':
            id = input('Account number: ')
            account = getAccountObj(id)
            if account:
                amount = input('Amount: ')                
                account.deposit(amount)
                print('Your amount was deposited!')
            else:
                print 'No such account found'
        elif choice == '4':
            id = input('Account number: ')
            account = getAccountObj(id)
            if account:
                amount = input('Amount: ')                
                if account.withdraw(amount):
                    print('Your amount was withdrawn!')
                else:
                    print('The amount could not be withdrawn')
            else:
                print 'No such account found'
        elif choice == '5':
            id = input('Account number: ')            
            account = getAccountObj(id)
            if account:
                statements = account.getStatements()
                for statement in statements:
                    print("ID|Account|Transaction|Amount|Date")
                    print(str(statement[0]) + "|" + str(statement[2]) + "|" + str(statement[3]) + "|" + str(statement[4]) + "|" + str(statement[5]))
            else:
                print 'No such account found'
            pass
        elif choice == '6':
            id = input('Account number: ')            
            account = getAccountObj(id)
            if account:
                account.closeAccount()
                print('Account closed!')
            else:
                print 'No such account found'
            pass
        elif choice == '7':
            pass
        else:
            print 'Invalid option!'

def adminMenu():
    choice = -1

    while choice != '3':
        print('\n')
        print('1.Print closed account history')
        print('2.Customers without CA')        
        print('3.Admin Logout')

        choice = raw_input('Enter your choice: ')
        if choice == '1':
            accounts = Account.getClosedAccounts()
            for account in accounts:
                print("Account|Account Type|Closed Date")
                print(str(account[0]) + "|" + str(account[2]) + "|" + str(account[6]))
        elif choice == '2':
            query = "SELECT * FROM users WHERE id NOT IN ( SELECT user_id FROM accounts WHERE type = 'CA' )"
            cur = db.getCursor()
            cur.execute(query)
            users = cur.fetchall()
            print("Id|First Name|Last Name")
            for user in users:
                print(str(user[0]) + "|" + str(user[1]) + "|" + str(user[2]))
        elif choice == '3':
            pass
        else:
            print('Invalid option!')

def mainMenu():
    choice  = -1    
    current_user = -1

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
                    current_user = id
                    userMenu(current_user)
                    break            
                else:
                    print('Invalid credentials!')
                attempts += 1
            else:
                print('Max sign in attempts reached')
        elif choice == '3':
            attempts = 1
            while attempts <=3:
                print("Attempt %d: "%(attempts))
                username = raw_input('Username: ')
                password = raw_input('Password: ')
                if Admin.authenticate(username, password):
                    # show admin related menu
                    adminMenu()                    
                    break            
                else:
                    print('Invalid credentials!')
                attempts += 1
            else:
                print('Max sign in attempts reached')
        elif choice == '4':
            pass
        else:
            print('Invalid option!')

# display main menu
mainMenu()

