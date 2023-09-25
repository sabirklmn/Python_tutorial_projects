# bank operation using OOP

class Bank:
    bankname="Indain Express Bank"
    branch="A23,BBSR,India"


    #create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f'Hello {self.username}cong! your account created succesfully')

    #deposit
    def deposit(self,amount):
            
        
        self.balance=self.balance+amount
            
        print(f'{amount} deposted succesfully')


    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw succesfully')
        else:
            print('Insufficent Fund...')


    #ministatement
    def minisatement(self):
        print(f' Your account balance is {self.balance}')


print(f'Welcome to {Bank.bankname} , {Bank.branch}')
username=input('Enter your name: ')
pan=input('Enter Pan card number: ')
address=input('Enter Your address: ')


b=Bank(username,pan,address)


while True:
    print('Please Selecte any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n44.Stop')
    option=int(input(''))

    if option==1:
        amount=float(input('Enter Deposited amount : '))

        b.deposit(amount)
    if option==2:
        amount=float(input('Enter Withdraw amount: '))
        b.withdraw(amount)
    
    if option==3
        b.minisatement()

    if option==4:
        print("Thanks for using Indian Expreess Bank... ")
        break
    else:
        print('Invaild option plz select a vaild option')