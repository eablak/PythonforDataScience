import datetime

datetime_now = datetime.datetime.now()

# print(datetime_now)

# print(datetime_now.year, "-" ,datetime_now.strftime("%Y"))
# print(datetime_now.month, "-", datetime_now.strftime("%B"))
# print(datetime_now.hour, datetime_now.minute, "-" ,datetime_now.strftime("%H:%M"))

print(f"Seconds since January 1, 1970: {datetime_now.timestamp():,.4f} or {datetime_now.timestamp():.2e} in scientific notation")
print(datetime_now.strftime("%b %d %Y"))