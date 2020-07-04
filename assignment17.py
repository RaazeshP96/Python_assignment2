'''
Write a program that serves as a basic calculator. 
It asks for two numbers, then it asks for an operator. 
Gracefully deal with input that doesn't cleanly convert to numbers. 
Deal with division by zero errors

'''


def calculator(num1, num2, optr):
    if optr == '+':
        return num1+num2
    elif optr == '-':
        return num1-num2
    elif optr == '*':
        return num1*num2
    elif optr == '/':
        try:
            return num1/num2
        except ZeroDivisionError:
            return 'You cannot divide number by zero'
    else:
        return "Something is wrong in input "


num1 = int(input("enter the first number:"))
optr = input("enter the operator:")
num2 = int(input("enter the second number:"))

print(calculator(num1, num2, optr))
