even = set(range(0, 40, 2))
print(sorted(even))
squared_tuple = (4, 6, 9, 16, 25)
squares = set(squared_tuple)
print(sorted(squares))

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# [4, 6, 9, 16, 25]


print("Even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("=========")

print("Squares minus even")
print(squares.difference(even))
print(squares - even)



# Even minus squares
# [0, 2, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# [0, 2, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# =========
# Squares minus even
# {9, 25}
# {9, 25}