# Basic Calculator:
# This script takes two numbers and an operator from the user, 
# then performs the selected arithmetic operation (+, -, *, /).

def calcolat() :

    print('\n*** Welcome to the calcolat ***\n')    
    a=int(input('Enter the frist number : '))
    c=input('Enter the type calcolat : ')
    b=int(input('Enter the scend number : '))

    print('*************')
  
    if c=="+" :
        print(f"{a} + {b} = {a+b}")
    elif c =='-' :
        print(f"{a} - {b} = {a-b}")
    elif c=='/' :
         print(f"{a} / {b} = {a/b}")
    elif c =='*' :
       print(f"{a} * {b} = {a*b}")
    else :
        print('Invalid input')

calcolat()