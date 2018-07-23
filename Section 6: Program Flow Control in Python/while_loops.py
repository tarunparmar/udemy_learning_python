# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1


available_exits = ["east", "north east", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you got out of there!")



## quiz
value = 8
ans = 0

for x in range(1, 13):
    ans = value * x
    print("{0} times {1} is {2}".format(x, value, ans))