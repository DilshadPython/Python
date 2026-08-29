"""
Demonstrates shallow copying dictionaries using dict.copy().
"""

def demo_copy_dict():
    month_table = {
        'Jan': 'January',
        'Feb': 'February',
        'Mar': 'March',
        'Apr': 'April',
        'May': 'May',
        'Jun': 'June',
        'Jul': 'July',
    }

    # Shallow copy creates an independent dictionary object
    copied_table = month_table.copy()
    print('Original month table keys:', list(month_table.keys()))
    print('Copied table:', copied_table)

    return month_table, copied_table

if __name__ == '__main__':
    demo_copy_dict()
