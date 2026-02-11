name = input("What is your name? ").strip()

# when you enter full name you have to type , between than is true and swapped
if "," in name:
    lname, fname = name.split(", ")
    # we swap the fname to come first and lname as second name in other word format it
    name = f"{fname} {lname}"

print(f"Your name is, {name}")

# here we jump one tab forward
print('\n\tTab')

# when we add r (regular Expression) the tab not work in the print
print(r'\n\tTab')

