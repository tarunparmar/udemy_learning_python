
# odd = range(0, 10000, 2)
# print(odd)
#
# print(odd[985])
#
# sevens = range(7, 100000, 7)
# x = int(input("Please enter a positive number less than 1 million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))


o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)