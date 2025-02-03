def main():
    yell(['Welcome', 'to', 'Python', 'in', '2025'])

def yell(texts):
    collection = []
    for text in texts:
        collection.append(text.upper())
    print(collection)
    # to display all in one line we have to use unpack *
    print(*collection)

if __name__ == '__main__':
    main()