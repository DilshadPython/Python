import re

url = input("URL: ").strip()

# username = url.replace("http://twitter.com/", "")
username = url.removeprefix("http://twitter.com/")

print(f"Username: {username}")

