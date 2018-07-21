
## 1
# name = input("Please enter your name: ")
# age = input("How old are you, {0}?".format(name))
# print(age)

# Please enter your name: T
# How old are you, T?2
# 2


## 2
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}?".format(name)))
# print(age)
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18-age))

# Please enter your name: T
# How old are you, T?15
# 15
# Please come back in 3 years


## 3

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guess it")
#     else:
#         print("Sorry you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guess it.")
#     else:
#         print("Sorry you have not guessed correctly")
# else:
#     print("You got it first time")


# Please guess a number between 1 and 10:
# 12
# Please guess lower
# 11
# Sorry you have not guessed correctly



## 4 - advanced ifelse

age = int(input("How old are you? "))

# if (age >=16) and (age <=65):
# if 16 <= age <=65:
#     print("Have a good day at work")


if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")


# How old are you? 45
# Have a good day at work


