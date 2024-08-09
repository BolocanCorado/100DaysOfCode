import random

print("Welcome to the password generator!")

letters = ['a', 'b', 'c' ,'s', 'w', 'h', 'k']
numbers = ['1', '2', '3', '4', '5', '6']
symbols = ['!', '@', '#', '$', '^']

lettersWanted = int(input("How many letters do you want in your password? "))
numbersWanted = int(input("How many numbers do you want in your password? "))
symbolsWanted = int(input("How many symbols do you want in your password? "))

passwordGenerated = []

for char in range(0, lettersWanted):
    passwordGenerated.append(random.choice(letters))
for char in range(0, numbersWanted ):
    passwordGenerated.append(random.choice(numbers))
for char in range(0, symbolsWanted ):
    passwordGenerated.append(random.choice(symbols))

random.shuffle(passwordGenerated)
password = ""

for i in passwordGenerated:
    password += i

print(f"You password generated is : {password}")