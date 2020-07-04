'''
Imagine you are designing a banking application. What would a customer
look like? What attributes would she have? What methods would she have?

'''
from datetime import date


class Customer:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.accNo = ''

    def enterDetail(self):
        self.name = input("Enter your name:")
        self.address = input("Enter your address:")
        self.accNo = input("Enter your account number:")

    def display(self):
        print(f'Name: { self.name }')
        print(f'Address: { self.address }')
        print(f'Account No: { self.accNo }')


c1 = Customer()
c1.enterDetail()
c1.display()
