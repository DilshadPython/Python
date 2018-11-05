import json


details = '''
{
    "properties": {
        "firstName": {
            "type": "string",
            "fname": "Dilshad"
        },
        "lastName": {
            "type": "string",
            "lname": "Abdulla"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        }
    },
    "required": ["firstName", "lastName"]
}
'''

data = json.loads(details)
# tested it works
print(data)
print('')

# another test to read the data type
print(type(data['required']))

print('')
print('####################')
for properties in data['properties']:
    print(properties)

print('')
print('####################')
for key, value in data.items():
    print(key, value)
