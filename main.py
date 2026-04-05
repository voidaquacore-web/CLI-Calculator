import os

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

while True:
    choice = input(" choose: [h] -> history | [e] -> exit | [c] -> to calculate: ")
    
    if choice.lower() == "e":
        save = input("save history? [y] -> yes | [n] -> no: ").lower() == "y"

        if not save:
            try:
                os.remove("history.txt")
            except FileNotFoundError:
                pass
        
        print("sayonara")
        break
    
    elif choice.lower() == "c":

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        operand = get_operand()

        result = operation(operand, num1, num2)    
                
        with open("history.txt" , "a") as file:
            file.write(f"{num1} {operand} {num2} = {result}" + "\n")

        
        print("")
        print(f"{num1} {operand} {num2} = {result}")
        print("")
      
    
    elif choice.lower() == "h":
        if os.path.exists("history.txt"):
            i = 1
            print("==== history ====")
            with open("history.txt" , "r") as f:
                for line in f:
                    print(f"{i}. {line}")
                    i += 1
        else:
            print("no calculations have been performed.")
    else:           
        print("invalid input, Try again!")
 
        


    
  


