'''COMPSCI 1MD3 Assignment 3: Two functions, a calculator and a number converter.

The calculator function is a chatterbox function which allows the user to perform basic arithmetic.
The number converter function takes in two arguments, a number in base-10 and a new base, then returns a string
which represents the converted number in the new base.

Faris Abuain, McMaster University, June 2024.'''



## Calculator Function

def calculator():
    ''' Calculator: a chatterbox function which allows user to add, subtract, multiply and divide two numbers
    until they quit the calculator. Also allows user to clear current display.
    
    Parameters: none
    
    Returns: none
    
    Output: displays currrent value, user operation options, and prompts for user input. Also prints 'Goodbye'
    if user quits, and '*** Invalid option' if user enters an invalid input.
    
    '''
    disp = 0.0 # initialize display value (starts as '0'; float)
    q = False # initialize 'quit' variable (ends loop when 'Q'/'q' is entered by user)
    while q == False:
        print(disp) # print current value to be displayed
        operation = str(input("(+)add, (-)subtract, (*)multiply, (/)divide, (C)clear, (Q)quit: "))
        if operation not in ['+', '-', '*', '/', 'Q', 'q', 'C', 'c']:
            print('*** Invalid option') # allows user to try again if they enter an invalid input
        elif operation == 'Q' or operation == 'q':
            print('Goodbye!')
            q = True # when user enter 'Q'/'q', calculator quits by ending while loop
        elif operation == 'C' or operation == 'c':
            disp = 0.0 # returns display value to 0.0 if user clears
        ## Arithmetic Operations
        else:
            num = float(input("Enter a number: "))
            if operation == '+':
                disp += num
            elif operation == '-':
                disp -= num
            elif operation == '*':
                disp = disp*num
            elif operation == '/':
                disp = disp/num
        print('') # for aesthetic purposes

calculator()


## Converter Function

def convert_base(d,b):
    ''' Convert Base: converts a number in base_10 to a number in a given base.

    Parameters:
        d (the number in base 10 we wish to convert)
        b (the base of the new number)
        
    Returns:
        False (if base is less than 2 or greater than 36)
        s (if 2<=b<37; string which represents converted number)
        
    Outputs:
        none
        
    '''
    s = '' # intialize 's' (represents converted number) as an empty string
    if b<2 or b>=37: 
        return False # returns 'false' if base is <2 or >=37
    ## Number Conversion Algorithm
    while d != 0:
        next_digit = d%b
        if next_digit < 10:
            next_digit = str(next_digit)
            s = next_digit + s # adds new character to left side of 's'
        elif next_digit >= 10:
            next_digit -= 10
            next_digit += ord('A')
            next_digit = chr(next_digit)
            s = next_digit + s # adds new character to left side of 's'
        d = d // b
    return s # return the converted number as a string

print(convert_base(1917, 24))
