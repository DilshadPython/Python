def main():
    yell('Welcome', 'to', 'Python', 'in', '2025')

def yell(*texts):
    # we use map function instead of for loops
    collection = map(str.upper, texts)

    # to display all in one line we have to use unpack *
    print(*collection)

if __name__ == '__main__':
    main()