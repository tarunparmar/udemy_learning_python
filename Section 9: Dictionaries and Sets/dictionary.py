fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])

# {'orange': 'a sweet, orange, citrus fruit', 'apple': 'good for making cider', 'lemon': 'a sour, yellow citrus fruit', 'grape': 'a small, sweet fruit growing in bunches', 'lime': 'a sour, green citrus fruit'}
# a sour, yellow citrus fruit


bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])



# to delete use del command
del fruit["lemon"]
print(fruit)


while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key)
    print(description)


# Please enter a fruit: grape
# a small, sweet fruit growing in bunches
# Please enter a fruit: apple
# good for making cider
#     Please enter a fruit: quit
#
# Process finished with exit code 0



while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)



print(fruit.keys())

# dict_keys(['orange', 'apple', 'grape', 'lime'])

print(fruit.values())

# dict_values(['a sweet, orange, citrus fruit', 'good for making cider', 'a small, sweet fruit growing in bunches', 'a sour, green citrus fruit'])




print(fruit.items())

# dict_items([('orange', 'a sweet, orange, citrus fruit'), ('apple', 'good for making cider'), ('grape', 'a small, sweet fruit growing in bunches'), ('lime', 'a sour, green citrus fruit')])

f_tuple = tuple(fruit.items())
print(f_tuple)

# (('orange', 'a sweet, orange, citrus fruit'), ('apple', 'good for making cider'), ('grape', 'a small, sweet fruit growing in bunches'), ('lime', 'a sour, green citrus fruit'))



for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

# orange is a sweet, orange, citrus fruit
# apple is good for making cider
# grape is a small, sweet fruit growing in bunches
# lime is a sour, green citrus fruit

print(dict(f_tuple))

# {'orange': 'a sweet, orange, citrus fruit', 'apple': 'good for making cider', 'grape': 'a small, sweet fruit growing in bunches', 'lime': 'a sour, green citrus fruit'}




