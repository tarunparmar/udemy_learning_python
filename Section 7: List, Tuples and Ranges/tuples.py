# t = "a", "b", "c"
# print(type(t))
# print(t[1])
#
# print("a", "b", "c")
# print(type(["a", "b", "c"]))


welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Night flight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])


# metallica[0] = "Master of puppets"

# Output:
# Results in error as Tuple is immutable
# Traceback (most recent call last):
# File "/home/tarun/IdeaProjects/udemy_learning_python/Section 7: List, Tuples and Ranges/tuples.py", line 21, in <module>
# metallica[0] = "Master of puppets"
# TypeError: 'tuple' object does not support item assignment



# Way to update tuple

imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)
print(len(imelda))

# Using list instead would let you update it
metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)


# Unpacking the tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)

# More Mayhem
# Imelda May
# 2011


# Example doesnt work well with Lists
# metallica2.append("Rock")   # .append only works with list
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)

# Traceback (most recent call last):
# File "/home/tarun/IdeaProjects/udemy_learning_python/Section 7: List, Tuples and Ranges/tuples.py", line 58, in <module>
# title, artist, year = metallica2
# ValueError: too many values to unpack (expected 3)



imelda = "More Mayhem", "Imilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, 'Kentish own Waltz')
title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)


# More Mayhem
# Imilda May
# 2011
# (1, 'Pulling the Rug')
# (2, 'Psycho')
# (3, 'Mayhem')
# (4, 'Kentish own Waltz')


# OR

imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
    (4, 'Kentish own Waltz'))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    # print("\t", song)
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))


# More Mayhem
# Imilda May
# 2011
# Track number 1, Title: Pulling the Rug
# Track number 2, Title: Psycho
# Track number 3, Title: Mayhem
# Track number 4, Title: Kentish own Waltz


