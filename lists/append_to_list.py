"""
Demonstrates dynamic list population using append() inside loops.
"""

def build_number_list(limit=5):
    # Initialize empty list
    numbers = []
    
    # Dynamically append elements
    for i in range(1, limit + 1):
        numbers.append(i * 10)
        
    print(f'Generated list up to {limit} items:', numbers)
    return numbers

if __name__ == '__main__':
    build_number_list()
