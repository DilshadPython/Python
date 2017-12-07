# while relationalExpression:
#     statments

# count-controlled
# event-controlled


while True:
    print("Please end a name?")
    answer = input(" ")
    if answer == "Raffi":
        print("You guessed it!")
        break
    else:
        print("No, not that word...")
        continue

'''
OUTPUT
python3 while.py 
Please end a name?
 Raffi
You guessed it!
'''