#Remove duplicated element from list
print("Eliminate duplicated element from list")
fruites = ["Apple", "Peach", "Pear", "Apple", "apple", "Malon"]
fructe = []
for fruit in fruites:
    if fruit not in fructe:
        fructe.append(fruit)
print(fructe)

