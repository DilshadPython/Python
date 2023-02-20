import json


with open('my_data.txt') as readme:
    js_data = json.load(readme)

print(js_data)

    # for x in data:
    #     print(x[''], '-', x[''])
