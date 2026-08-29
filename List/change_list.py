"""
Demonstrates list mutability by modifying elements by index position.
"""

def demo_modify_by_index():
    colors = ['red', 'green', 'blue']
    print('Before modification:', colors)

    # Modify single element in-place
    colors[1] = 'yellow'
    print('After colors[1] = "yellow":', colors)

    # Modify slice in-place
    colors[0:2] = ['purple', 'orange']
    print('After slice modification colors[0:2]:', colors)

    return colors

if __name__ == '__main__':
    demo_modify_by_index()
