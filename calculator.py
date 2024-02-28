num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
opr = str(input("enter operation (+,-,*,/)=>"))
if opr == "+" :
    print("The Addition of two numbers is",num1 + num2)
elif opr == "-" :
    print("The subtraction of two numbers is",num1 - num2)
elif opr == "*" :
    print("The multiplication of two numbers is",num1 * num2)
elif opr == "/" :
    print("The division of two numbers is",num1 / num2)
else:
    print("invalid input")   