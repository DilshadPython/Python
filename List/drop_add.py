"""
Demonstrates combination of drop (pop/remove) and add (append/insert) methods.
"""

def demo_drop_add():
    queue = ['Customer 1', 'Customer 2', 'Customer 3']
    print('Initial queue:', queue)

    # Remove customer by name
    queue.remove('Customer 2')
    print('After remove("Customer 2"):', queue)

    # Add VIP customer at head of line
    queue.insert(0, 'VIP Customer')
    print('After insert(0, "VIP Customer"):', queue)

    # Serve first customer (pop at index 0)
    served = queue.pop(0)
    print(f'Served customer: {served}')
    print('Remaining queue:', queue)

    return queue

if __name__ == '__main__':
    demo_drop_add()
