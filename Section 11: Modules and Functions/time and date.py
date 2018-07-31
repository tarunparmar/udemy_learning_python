import time

print(time.gmtime(0))
print(time.localtime())
print(time.time())


# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# time.struct_time(tm_year=2018, tm_mon=7, tm_mday=30, tm_hour=22, tm_min=59, tm_sec=3, tm_wday=0, tm_yday=211, tm_isdst=1)
# 1533009543.820538


# timezone

from time import timezone
print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], timezone))

if time.daylight != 0 :
    print("\tDaylight Saving is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))



# The epoch on this system starts at Thu Jan  1 00:00:00 1970
# The current timezone is CST with an offset of 21600
# Daylight Saving is in effect for this location
#     The DST timezone is CDT
# Local time is 2018-07-30 23:11:11
# UTC time is 2018-07-31 04:11:11




# datetime

import  datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

# 2018-07-30 23:16:12.733677
# 2018-07-30 23:16:12.733723
# 2018-07-31 04:16:12.733735




