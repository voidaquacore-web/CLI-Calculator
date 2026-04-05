print("---------- Calculator -----------")

def operation(operand, num1, num2):
    if operand == "+":
        return num1 + num2
    elif operand == "-":
        return num1 - num2
    elif operand == "/":
        if num2 == 0:
            print("cannot divide by zero")
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
       operand = input("choose operation (+,-,*,/): ")
       if operand in ["+","-","/","*"]:
           break
       else:
           print("invaild operator (-,+,/,* only)")
    return operand

history = []

while True:
    choice = input(" choose: [h] -> history | [e] -> exit | [c] -> to calculate: ")
    
    if choice.lower() == "e":
        print("sayonara")
        break
    
    elif choice.lower() == "c":

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        operand = get_operand()

        result = operation(operand, num1, num2)    
                
        history.append((num1,operand, num2, result))

        if isinstance(result, int) or isinstance(result, float):
            print("")
            print(f"{num1} {operand} {num2} = {result}")
            print("")
        else:
            print(result)
    
    elif choice.lower() == "h":
        i = 1
        if not history:
            print("No calculations performed yet.")
        else:
            print("History ->")
            for calc in history:
                a, op, b , result = calc
                print(f"{i}. {a} {op} {b} = {result}")
                i += 1
            print('')
    else:
        print("invalid input, Try again!")
 
        


    
  


