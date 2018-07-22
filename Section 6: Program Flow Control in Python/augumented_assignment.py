number = "9, 223, 373, 036, 854, 775, 807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The number is {} ".format(newNumber))



x = 23
x+= 1
print(x)


greeting = "Good "
greeting += "Morning"
print(greeting)

greeting *= 5
print(greeting)