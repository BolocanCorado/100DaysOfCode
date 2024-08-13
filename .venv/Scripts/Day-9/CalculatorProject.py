def add (n1, n2):
    return n1 + n2
def minus (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def devide (n1, n2):
    return n1 / n2

operations = {"+":add,
              "-":minus,
              "*":multiply,
              "/":devide
              }

def calculator ():

    again = True
    num1 = float(input("Add first number: \n"))
    while again:
        operationWanted = input("Which operation do you want?: '+', '-', '*' or '/' :\n")
        num2 = float(input("Add second number: \n"))
        for symbol in operations:
            if symbol == operationWanted:
                output = operations[operationWanted](num1, num2)
                print("\n" * 5)
                print(f"{num1} {operationWanted} {num2} = {output}")
                wantAgain = input(f"Want keep {output} and continue calculating? 'yes' or 'no' :\n").lower()
                if wantAgain == "yes":
                    num1 = output
                elif wantAgain == "no":
                    again = False
                    print("\n" * 20)
                    print("Starting calculating")
                    calculator()

calculator()






