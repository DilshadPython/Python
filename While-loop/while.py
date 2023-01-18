# while relationalExpression:
#     statments

# count-controlled
# event-controlled


while True:
    print("Please enter a name of your pets start with R and ended with i ?")
    answer = input(" ")
    if answer == "Raffi":
        print("You guessed it!")
        break
    else:
        print("No, wrong name...")
        continue

'''
OUTPUT
python3 while.py 
Please end a name?
 Raffi
You guessed it!
'''
