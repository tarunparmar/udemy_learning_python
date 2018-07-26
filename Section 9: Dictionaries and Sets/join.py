
## join

mylist = ["a", "b", "c", "d"]

newStr = ''
for c in mylist:
    newStr += c+ ", "

print(newStr)

## Above code is not efficient way to code
## So should use join

print("=========")
newStr = "\n".join(mylist)
print(newStr)


print("=========")
## another example


locations = {0: "You're sitting in front of a computer",
             1: "You're standing at end of road",
             2: "You're at top of a hill",
             3: "You're inside a building",
             4: "You're in a valley beside a stream",
             5: "You're in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")


