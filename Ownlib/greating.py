from names import actor
from names import name

def main():
    print("I call a name wrote in names file")
    morning()
    night()


def morning():
    print("Good morning ", name)

def night():
    print("Good night ", actor)

if __name__ == "__main__":
    main()