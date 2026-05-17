'''
Create a method that swap the index of list contain random number and entered manually,
 the length of list less than 10 numbers. The concept is do not use reverse()
 function created by python.
Example:
Enter number 1: 25
Enter number 2: 14
Enter number 3: 3
Enter number 4: 6
Enter number 5: 87
Created List: [25, 14, 3, 6, 87]

Swapped List: [87, 6, 3, 14, 25]
'''
import random

def swap_index(numbers):

    # define the first item
    start_index = 0
    # define the last item
    end_index = len(numbers) - 1

    while start_index < end_index:
        # we start to swap the them
        numbers[start_index], numbers[end_index] = numbers[end_index], numbers[start_index]
        start_index += 1
        end_index -= 1

# Random length less than 10
length = random.randint(0, 10)
numbers = []

for i in range(length):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

if __name__ == '__main__':
    print("Created List:", numbers,'\n')
    swap_index(numbers)
    print("Swapped List: ", numbers)
