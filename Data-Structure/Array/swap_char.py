def swap_index(characters):

    # define the first item
    start_index = 0
    # define the last item
    end_index = len(characters) - 1

    while start_index < end_index:
        # we start to swap the characters index
        characters[start_index], characters[end_index] = characters[end_index], characters[start_index]
        start_index += 1
        end_index -= 1

if __name__ == '__main__':
    # define the list of array
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
    print(characters, '\n')
    # swapped
    swap_index(characters)
    # display
    print(characters)