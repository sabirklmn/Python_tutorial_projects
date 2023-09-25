# bank operation using OOP

class Bank:
    bankname="Indain Express Bank"
    branch="A23,BBSR,India"


    #create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
       # self.balance=0.0
        print(f'Hello {self.username}cong! your account created succesfully')



username=input('Enter your name: ')
pan=input('Enter Pan card number: ')
address=input('Enter Your address: ')


b=Bank(username,pan,address)