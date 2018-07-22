for i in range(1,20):
    print("i is now {}".format(i))

# i is now 1
# i is now 2
# i is now 3
# i is now 4
# i is now 5
# i is now 6
# i is now 7
# i is now 8
# i is now 9
# i is now 10
# i is now 11
# i is now 12
# i is now 13
# i is now 14
# i is now 15
# i is now 16
# i is now 17
# i is now 18
# i is now 19


number = "9, 223, 372, 036, 854"
for i in range(0, len(number)-1):
    print(number[i])

# 9
# ,
#
# 2
# 2
# 3
# ,
#
# 3
# 7
# 2
# ,
#
# 0
# 3
# 6
# ,
#
# 8
# 5


number = "9, 223, 372, 036, 854"
cleanedNumber = ''
for i in range(0, len(number)-1):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

# The number is 922337203685



## Extending for loops

