print("---------- Calculator -----------")

def operation(operand, num1, num2):
    if operand == "+":
        return num1 + num2
    elif operand == "-":
        return num1 - num2
    elif operand == "/":
        if num2 == 0:
            return "cannot divide by zero"
        return num1 / num2
    elif operand == "*":
        return num1 * num2
    
def get_number(msg):
    while True:
        try:
          num = int(input(msg))
          break
        except ValueError:
            print("invalid number, try again")
    return num

def get_operand():
    while True:
       operand = input("which operation? (+,-,*,/): ")
       if operand in ["+","-","/","*"]:
           break
       else:
           print("invaild operator (-,+,/,* only)")
    return operand


while True:
    
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    
    operand = get_operand()

    result = operation(operand, num1, num2)    
            

    if isinstance(result, int) or isinstance(result, float):
        print(f"{num1} {operand} {num2} = {result}")
    else:
        print(result)
    
    exit = input("Do you want to exit? (y/n) : ")
    if exit.lower() == "y":
        print("sayonara")
        break
    
        


    
  


