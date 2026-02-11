import re


urls = '''
http://twitter.com/username+
https://google.com
http://youtube.com
https://www.gov.uk
http://cambridge.edu
'''

# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# or
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)

find_all = pattern.findall(urls)

for find in find_all:
    print('\n\t find all ', find)

for match in matches:
    print('\n\t ', match)

                    # \2 group 2  \3 group 3
subbed_urls = pattern.sub(r'\t\2\3', urls)

print(subbed_urls)

