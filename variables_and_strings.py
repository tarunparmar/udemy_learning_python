a = 12
b = 3
print(a+b)
print(a/b)
print(a//b)
print(a%b)

print((((a+b) / 3) - 3) * 12)


parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[0:3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-1])
print(parrot[0:6:2])
print(parrot[0:6:3])

## extract comma only
n = "9, 123, 564, 567, 763"
print(n[1::5])

## Avoid comma and space
n = "1, 2, 3, 4, 5"
print(n[0::3])


# Multiple string
print("Hello " * 5)
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)
print("fri" in today) # results in True
print("thu" in today) # results in False
