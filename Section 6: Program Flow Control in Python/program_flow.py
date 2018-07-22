# part 1

# challenge

# ipAddress = input("Please enter ip address: ")
# segment = 1
# seg_length = 0
# character = ''
#
# for character in ipAddress:
#     if character == '.':
#         print("segment: {} contains {} characters".format(segment, seg_length))
#         segment += 1
#         seg_length = 0
#     else:
#         seg_length += 1
#
# # unless the final character in string was a . then we haven't print last segment
# if character != '.':
#     print("segment: {} contains {} characters".format(segment, seg_length))
#


## Part 2


ipAddress = input("Please enter ip address: ")
ipAddress += '.'
segment = 1
seg_length = 0
# character = ''

for character in ipAddress:
    if character == '.':
        print("segment: {} contains {} characters".format(segment, seg_length))
        segment += 1
        seg_length = 0
    else:
        seg_length += 1

# unless the final character in string was a . then we haven't print last segment
# if character != '.':
#     print("segment: {} contains {} characters".format(segment, seg_length))


# output
# Please enter ip address: 123.4567.8.9.
# segment: 1 contains 3 characters
# segment: 2 contains 4 characters
# segment: 3 contains 1 characters
# segment: 4 contains 1 characters
# segment: 5 contains 0 characters



ipAddress = input("Please enter ip address: ")
if ipAddress[-1] != '.':
    ipAddress += '.'
segment = 1
seg_length = 0
# character = ''

for character in ipAddress:
    if character == '.':
        print("segment: {} contains {} characters".format(segment, seg_length))
        segment += 1
        seg_length = 0
    else:
        seg_length += 1
