print("---------- Calculator ----------")

def operation(operand, num1, num2):
    if operand == "+":
        return num1 + num2
    elif operand == "-":
        return num1 - num2
    elif operand == "/":
        return num1 / num2
    elif operand == "*":
        return num1 * num2
    else:
        return "wrong operand"
    
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
operand = input("which operation? (+,-,*,/): ")

result = operation(operand, num1, num2)

if result == int:
    print(f"{num1} {operand} {num2} = {result}")
else:
    print(result)

    
  


