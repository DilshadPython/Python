import re
'''
/Python/RegularEx$ py social_user.py 
URL: http://twitter.com/dilshadabdulla
Username: dilshadabdulla
/Python/RegularEx$ py social_user.py 
URL: https://www.twitter.com/dilshadabdulla
Username: dilshadabdulla

'''

url = input("URL: ").strip()

# re.sub(pattern, repl, string, count=0, flags=0)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
# or
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

