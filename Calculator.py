#python calculator of 2 numbers

#first number and error handling
try: 
    a = int(input('Enter first Number: ')) 
except ValueError:
    print('Error! Enter a valid number!')
    exit()
                    
#operator input and error handling
Operator = input('Enter operation eg +,-,*,/: ')
def checkOperator():
    valid_operators = ['+', '-', '/', '*']
    if Operator in valid_operators:
        return True
    else:
        return False
checkOperator()
# second number and error handling
try: 
    b = int(input('Enter Second Number: '))    
except ValueError: 
    print('Error! Enter a valid number!')             
    exit()

#function for calculation
def calculate():
    #try for error handling
    #F string is for combining variable and expression. Its a way of emmbeding a template literal.
    try: 
        if Operator == '+': #sum
            print(f"Your result is {a + b}")
        elif Operator == '-': #minus
            print(f"Your result is {a - b}")
        elif Operator == '*': #multiplication
            print(f"Your result is {a * b}")
        elif Operator == '/': #division
            if b != 0: #checks if b is 0;
                print(f"Your result is {a / b}")
            else:
                print('Not a valid number!')
        else:
            print('Error! Invalid operator')


    #error handling
    except ValueError:
        print('Error! Please enter valid numbers!')

#calling the function
calculate()
print('Done')





