import datetime

datetime_now = datetime.datetime.now()

print(
    f"Seconds since January 1, 1970: {datetime_now.timestamp():,.4f} "
    f"or {datetime_now.timestamp():.2e} in scientific notation"
)
print(datetime_now.strftime("%b %d %Y"))
