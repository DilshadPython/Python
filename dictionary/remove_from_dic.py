"""
Demonstrates removing items using dict.pop().
"""

def demo_pop_dict():
    month_table = {
        'Jan': 'January', 'Feb': 'February', 'Mar': 'March',
        'Apr': 'April', 'May': 'May', 'Jun': 'June', 'Jul': 'July'
    }

    # pop() removes the key and returns its associated value
    popped_val = month_table.pop('Mar')
    print('Popped value for "Mar":', popped_val)
    print('Remaining keys:', list(month_table.keys()))

    return popped_val, month_table

if __name__ == '__main__':
    demo_pop_dict()
