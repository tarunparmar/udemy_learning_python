string = "1234567890"

# for char in string:
#     print(char)

# my_iter = iter(string)
# print(next(my_iter)) # print one at a time
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


# for char in iter(string):
#     print(char)


## Create list of items, then create iterator using iter()
# Use a for loop to loop "n" times on list to print next item

# hint: use len() function rather than counting number of items in list

my_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
my_iter = iter(my_list)
for item in range(0, len(my_list)):
    next_item = next(my_iter)
    print(next_item)