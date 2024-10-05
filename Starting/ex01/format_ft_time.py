import datetime

now = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {now.timestamp():,.4f} or {now.timestamp():.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
print("aasd")