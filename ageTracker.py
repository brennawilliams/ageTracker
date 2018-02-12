nameage = {}
counter = 1

while counter < 6:
	name = input("Enter the name of friend " + str(counter) + ": ")
	age = input("Enter the age of friend " + str(counter) + ": ")
	nameage[name] = age
	counter = counter + 1

print("The contents of the database is: " + str(nameage))