from html.parser import HTMLParser
from urllib import parser

import urllib.request


class LinkParser(HTMLParser):
	pass

	# def starting(self, tag, attrs):
	# 	# we start visiting the pages to find all urls
	# 	if tag == 'a':
	# 		for (key, value) in attrs:
	# 			if key == 'href':
	# 				create_url = parse.urljoin(self.) 
