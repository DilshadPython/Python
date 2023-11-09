# while relationalExpression:
#     statments

# count-controlled
# event-controlled
while True:
    print("Please enter a name of the pets start with R ended with i ?")
    answer = input(" ")
    if answer == "Raffi":
        print("True this is correct!")
        break
    else:
        print("False, wrong name...")
        continue

'''
OUTPUT
python3 while.py 
Please end a name?
 Raffi
You guessed it!
'''
