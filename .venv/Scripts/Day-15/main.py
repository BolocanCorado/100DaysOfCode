import progRess

print("Welcome to Coffee Machine")
print("Here you can choose espresso/latte/cappucino")


def is_resources_available(resources):
    '''Checking if resources are enough for product chosen'''
    for item in resources:
        if resources[item] >= progRess.RESOURCES[item]:
            print(f"Sorry, there is not enought {item}")
            return False
    return True

def payment():
    '''Calculate amount of money that were iserted'''
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return round(total,2)

def updateResources(order_ingredients):
    '''After processing the product chosen, ingredients shall be updated'''
    for item in order_ingredients:
        progRess.RESOURCES[item] -= order_ingredients[item]


isOn = True
profit = 0
while isOn:
    askUser = input("What do you like? (espresso/latte/cappucino) 'report' or 'off': ")
    if askUser == "off":
        isOn = False
    elif askUser == "report":
        print(f"Milk: {progRess.RESOURCES['milk']}ml \n"
              f"Water: {progRess.RESOURCES['water']}ml \n"
              f"Coffee: {progRess.RESOURCES['coffee']}g \n"
              f"Profit: {profit}$")
    else:
        drink = progRess.MENU[askUser]['ingredients']
        #Checking if resources are available
        if is_resources_available(drink) == True:
            productPayment = payment()
            if productPayment < progRess.MENU[askUser]['cost']:
                print(f"You have entered {productPayment}$ and the price for {askUser} is {progRess.MENU[askUser]['cost']}$")
                print("Not enough money. Money refunds")
            elif productPayment > progRess.MENU[askUser]['cost']:
                changes = round(productPayment - progRess.MENU[askUser]['cost'], 2)
                profit += progRess.MENU[askUser]['cost']
                print(f"You have inserted {productPayment}$. Here is {changes}$")
                print(f"Enjoy your {askUser}")
                updateResources(drink)
            elif productPayment == progRess.MENU[askUser]['cost']:
                profit += progRess.MENU[askUser]['cost']
                print(f"You have inserted {productPayment}$")
                print(f"Enjoy your {askUser}")
                updateResources(drink)


