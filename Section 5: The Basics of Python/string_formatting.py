age = 24
# print("my age is " + age) # results in error
print("my age is " + str(age))

print("There are {0} days in {1}, {2}, {3} and {4}".format(31, "Jan", "Mar", "May", "Jul"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("My age is %d years" % age)

print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %d and cubed is %4d" %(i, i ** 2, i ** 3))

# 50 decimal points
print("Pi is approx. %12.50f" % (22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i ** 2, i ** 3))


# 50 decimal points
print("Pi is approx. {0:12.50}" .format(22 / 7))


# Quiz questions
meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""
print(meal1)
print(meal2)
print(meal3)
print(meal4)

print((10 * 5.0))
print((10 * 5.0) /5)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::1])
print(days[::3])
print(days[::5])


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[:-1:5])


flower = "blue violet"
print("blue" in flower) # will output True


flower = "rose"
colour = "red"

print("The {0} is {1}" .format(flower, colour))