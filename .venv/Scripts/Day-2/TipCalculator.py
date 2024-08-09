print("Welcome to the tip calculator!!!")
total_bill = float(input("What is your total bill? $  "))
tip_added = int(input("What is your tip added? 10,12,15,20$  "))
people = int(input("How many people? "))

print("Each person should pay: $  " + str((total_bill + tip_added) / people))
