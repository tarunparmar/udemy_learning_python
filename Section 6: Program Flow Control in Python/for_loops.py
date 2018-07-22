for i in range(1,20):
    print("i is now {}".format(i))

# i is now 1
# i is now 2
# i is now 3
# i is now 4
# i is now 5
# i is now 6
# i is now 7
# i is now 8
# i is now 9
# i is now 10
# i is now 11
# i is now 12
# i is now 13
# i is now 14
# i is now 15
# i is now 16
# i is now 17
# i is now 18
# i is now 19


number = "9, 223, 372, 036, 854"
for i in range(0, len(number)-1):
    print(number[i])

# 9
# ,
#
# 2
# 2
# 3
# ,
#
# 3
# 7
# 2
# ,
#
# 0
# 3
# 6
# ,
#
# 8
# 5


number = "9, 223, 372, 036, 854"
cleanedNumber = ''
for i in range(0, len(number)-1):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

# The number is 922337203685



## Extending for loops

number = "9, 223, 372, 036, 854"
cleanedNumber = ''
for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

# The number is 9223372036854



for state in ["not pinin'","no more","a stiff","bereft of life"]:
    print("This parrot is "+ state)

# This parrot is not pinin'
# This parrot is no more
# This parrot is a stiff
# This parrot is bereft of life



for i in range(1, 13):
    for j in range(1, 13):
        print("{1}x{0}={2}".format(i, j, i*j), end='\t')
    print('')


# 1x1=1	2x1=2	3x1=3	4x1=4	5x1=5	6x1=6	7x1=7	8x1=8	9x1=9	10x1=10	11x1=11	12x1=12
# 1x2=2	2x2=4	3x2=6	4x2=8	5x2=10	6x2=12	7x2=14	8x2=16	9x2=18	10x2=20	11x2=22	12x2=24
# 1x3=3	2x3=6	3x3=9	4x3=12	5x3=15	6x3=18	7x3=21	8x3=24	9x3=27	10x3=30	11x3=33	12x3=36
# 1x4=4	2x4=8	3x4=12	4x4=16	5x4=20	6x4=24	7x4=28	8x4=32	9x4=36	10x4=40	11x4=44	12x4=48
# 1x5=5	2x5=10	3x5=15	4x5=20	5x5=25	6x5=30	7x5=35	8x5=40	9x5=45	10x5=50	11x5=55	12x5=60
# 1x6=6	2x6=12	3x6=18	4x6=24	5x6=30	6x6=36	7x6=42	8x6=48	9x6=54	10x6=60	11x6=66	12x6=72
# 1x7=7	2x7=14	3x7=21	4x7=28	5x7=35	6x7=42	7x7=49	8x7=56	9x7=63	10x7=70	11x7=77	12x7=84
# 1x8=8	2x8=16	3x8=24	4x8=32	5x8=40	6x8=48	7x8=56	8x8=64	9x8=72	10x8=80	11x8=88	12x8=96
# 1x9=9	2x9=18	3x9=27	4x9=36	5x9=45	6x9=54	7x9=63	8x9=72	9x9=81	10x9=90	11x9=99	12x9=108
# 1x10=10	2x10=20	3x10=30	4x10=40	5x10=50	6x10=60	7x10=70	8x10=80	9x10=90	10x10=100	11x10=110	12x10=120
# 1x11=11	2x11=22	3x11=33	4x11=44	5x11=55	6x11=66	7x11=77	8x11=88	9x11=99	10x11=110	11x11=121	12x11=132
# 1x12=12	2x12=24	3x12=36	4x12=48	5x12=60	6x12=72	7x12=84	8x12=96	9x12=108	10x12=120	11x12=132	12x12=144




quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

# A
# S
# M
# E
# W
# P
# O
# I
# R
# F
# W
# S
# P
# H
# R

## Print all number between 0 to 100 that are divisible by 7

for i in range(0,100):
    if i % 7 == 0:
        print(i)

# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 77
# 84
# 91
# 98