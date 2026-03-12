def reverse_index(numbers):

    # define the first item
    start_index = 0
    # define the last item
    end_index = len(numbers) - 1

    while start_index < end_index:
        # we start to swap the them
        numbers[start_index], numbers[end_index] = numbers[end_index], numbers[start_index]
        start_index += 1
        end_index -= 1

if __name__ == '__main__':
    numbers = [1, 2, 3, -4, 5, -6, 7, 8, -9, 10]
    print(numbers, '\n')
    reverse_index(numbers)
    print(numbers)

