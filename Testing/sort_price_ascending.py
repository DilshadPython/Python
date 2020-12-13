'''
Implement the function sort_by_price_ascending, which:
- Accepts a string in JSON format, as in the example below.
- Orders items by price in ascending order.
- If two productes have the same price, it orders them by their name in alphabetical order.
- Returns a string in JSON format that is equivalent to the one on the input format.

For example, the call:

sort_by_price_ascending("
	[{'name': 'eggs', 'price': 1}, 
	{'name': 'coffee', 'price': 9.99}, 
	{'name': 'rice', 'price': 4.04}]
");

Should return:

"
	[
		{'name': 'eggs', 'price': 1}, 
		{'name': 'rice', 'price': 4.04},
		{'name': 'coffee', 'price': 9.99}
	]
"
'''

# Before
# def sort_by_price_ascending(json_string):
#     return None

# Solution
import json


json_string = [
			{'name': 'eggs', 'price': 1},
			{'name': 'coffee', 'price': 9.99},
			{'name': 'rice', 'price': 4.04}
		]


def sort_by_price_ascending(json_string):

    json_string = json.dumps(json_string)

    return json_string


print(sort_by_price_ascending(json_string))
