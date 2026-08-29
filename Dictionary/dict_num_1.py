"""
Demonstrates dynamic key assignment and numerical lookup.
"""

def demo_dynamic_keys():
    data = {}
    data['num'] = 22
    data['num1'] = 47
    data['num2'] = 10
    data['num3'] = 84
    data['num4'] = 65

    total = sum(data.values())
    max_val = max(data.values())

    print('Built data dict:', data)
    print('Total sum of values:', total)
    print('Max value:', max_val)

    return data, total, max_val

if __name__ == '__main__':
    demo_dynamic_keys()
