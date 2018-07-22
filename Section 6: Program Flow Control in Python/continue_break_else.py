# continue , break and else
#
# shopping_list = ["milk","pasta","eggs", "spam", "bread","rice"]
#
# for item in shopping_list:
#     if item == 'spam':
#         break
#
#     print("Buy " + item)


# Buy milk
# Buy pasta
# Buy eggs


## 2 - using break and else

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then please")

if nasty_food_item:
    print("Can't have anything without spam in it")


# Can't have anything without spam in it


## Continue test

# Write program to print out all number from 0 to 20 that aren't
# divisible by 3 or 5.

# using continue
for i in range(0,20):
    if i%3 ==0 or i%5 ==0:
        continue
    print(i)


# 1
# 2
# 4
# 7
# 8
# 11
# 13
# 14
# 16
# 17
# 19

## Without continue
for i in range(0,20):
    if i%3 !=0 and i%5 !=0:
        print(i)


# 1
# 2
# 4
# 7
# 8
# 11
# 13
# 14
# 16
# 17
# 19