fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}


print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit please"}

print(veg)

## update command to bind two dictionaries together
veg.update(fruit)

print(veg)

# {'orange': 'a sweet, orange, citrus fruit', 'apple': 'good for making cider', 'lemon': 'a sour, yellow citrus fruit', 'grape': 'a small, sweet fruit growing in bunches', 'lime': 'a sour, green citrus fruit'}
# {'cabbage': "every child's favorite", 'sprouts': 'mmmmm, lovely', 'spinach': 'can I have some more fruit please'}
# {'cabbage': "every child's favorite", 'sprouts': 'mmmmm, lovely', 'spinach': 'can I have some more fruit please', 'orange': 'a sweet, orange, citrus fruit', 'apple': 'good for making cider', 'lemon': 'a sour, yellow citrus fruit', 'grape': 'a small, sweet fruit growing in bunches', 'lime': 'a sour, green citrus fruit'}
