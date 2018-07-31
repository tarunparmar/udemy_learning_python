# jabber = open("sample.txt")
#
# for line in jabber:
#     print(line)
#
# jabber.close()


with open("sample.txt","r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')


# "Beware the Jabberwock, my son!
# The Jabberwock, with eyes of flame,
# "And hast thou slain the Jabberwock?



with open("sample.txt","a") as tables:
    for i in range(2,13):
        for j in range(2, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file = tables)
        print("-" * 20, file=tables)



with open("sample.txt","r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()