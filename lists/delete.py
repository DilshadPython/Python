"""
Demonstrates removing items or slices from a list using the 'del' statement.
"""

def demo_delete():
    data = [10, 20, 30, 40, 50, 60]
    print('Original data:', data)

    # Delete element at index 2 (30)
    del data[2]
    print('After del data[2]:', data)

    # Delete slice from index 1 to 3
    del data[1:3]
    print('After del data[1:3]:', data)

    return data

if __name__ == '__main__':
    demo_delete()
