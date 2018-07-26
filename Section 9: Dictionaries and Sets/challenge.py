

locations = {0: "You're sitting in front of a computer",
             1: "You're standing at end of road",
             2: "You're at top of a hill",
             3: "You're inside a building",
             4: "You're in a valley beside a stream",
             5: "You're in the forest"}

# convert from list to dictionary
# by removing [] and replace with {}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

print(locations[0].split())

# ["You're", 'sitting', 'in', 'front', 'of', 'a', 'computer']

print(locations[3].split(", "))

# ["You're inside a building"]

print(' '.join(locations[0].split()))
# You're sitting in front of a computer'

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits).upper()
    print()
    # PArse the user input, with out vocabulary dictionary
    if len(direction) > 1:
        for word in vocabulary:
            if word in direction:
                direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")


