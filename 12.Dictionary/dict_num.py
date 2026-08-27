"""
Demonstrates modifying numeric values stored in dictionary keys.
"""

def demo_numeric_dict():
    text = {'num': 5628, 'num1': -854, 'num2': 44}

    sub_res = text['num1'] - 12
    mul_res = text['num'] * 2

    # In-place increment of dictionary value
    text['num2'] += 44
    print('Updated text["num2"]:', text['num2'])

    return sub_res, mul_res, text['num2']

if __name__ == '__main__':
    demo_numeric_dict()
