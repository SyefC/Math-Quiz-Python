import random
import os

loopescape = 0
loopsub = 3
loophold = 0
signOperator = ''
num1 = random.randint(1,150)
num2 = random.randint(1,100)
operator = random.randint(1,4)

result = num1 + num2

if(operator == 1):
    signOperator = '+'
    result = num1 + num2
    operator = 0
elif(operator == 2):
    signOperator = '*'
    result = num1 * num2
    operator = 0
elif(operator == 3):
    signOperator = '-'
    result = num1 / num2
    operator = 0
elif(operator == 4):
    signOperator = '/'
    result = num1 - num2
    operator = 0

while(loophold != 1):
    inpo = float(input(f"{num1} {signOperator} {num2}: "))
    if(inpo == result):
        loopescape += 1
        loopsub -= 1
        print(f"You Got {loopescape} points {loopsub} way more to go!")
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        operator = random.randint(1,4)

        if(operator == 1):
            signOperator = '+'
            result = num1 + num2
            operator = 0
        elif(operator == 2):
            signOperator = '*'
            result = num1 * num2
            operator = 0
        elif(operator == 3):
            signOperator = '-'
            result = num1 / num2
            operator = 0
        elif(operator == 4):
            signOperator = '/'
            result = num1 - num2
            operator = 0

        if(loopescape == 3):
            loophold = 1
            os.system('cls')
            print("you won!")
    else:
        print("wrong!")
