import pytz
import datetime
country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.now()))


# The time in Europe/Moscow is 2018-07-31 07:36:48.359463+03:00
# UTC is 2018-07-30 23:36:48.359524


for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
