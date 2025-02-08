# Simple Calculator For Basic Arithmetic Operations
try: # To Check Whether any error occurs using try Block 
    # Two Inputs from user
    number1=float(input("Enter the First Number : "))
    number2=float(input("Enter the Second Number : "))
# Menu
    print("""1.Addition(+)
2.Subtraction(-)
3.Multiplication(x)
4.Division(/)
 """)
    
    user_choice=input("Enter the option(1/2/3/4) : ") # User Enter the choice
    if user_choice=="1":
        print(f"Addition:{number1+number2}") # Addition
    elif user_choice=="2":
        print(f"Subtraction:{number1-number2}") # Subtraction
    elif user_choice=="3":
        print(f"Multiplication:{number1*number2}") # Multiplication
    elif user_choice=="4":
        print(f"Division:{number1/number2}") # Division
    else:
        print("Incorrect Choice!")
# If Error Occurs except Block Will Handle it.
except ZeroDivisionError :
    print("Sorry Can't divide by Zero.")
except ValueError :
    print("Sorry Wrong Input.")
