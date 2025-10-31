


def user_detail(fname: str, lname: str, age: int) -> dict:
    email = f"{fname.lower()}.{lname.lower()}@example.com"
    
    return {
        'fname': fname,
        'lname': lname,
        'email': email,
        'age': age,
    }
    
user = user_detail("Jane", "Doe", 28)
print(user)

first_user = user_detail("Tom", "David", "thirty-one")
print(first_user)

# Python/TypeHints$ mypy type.py 
# Ptype.py:17: error: Argument 3 to "user_detail" has incompatible type "str"; expected "int"  [arg-type]
# Python/TypeHints$ python type.py 
# {'fname': 'Jane', 'lname': 'Doe', 'email': 'jane.doe@example.com', 'age': 28}
# {'fname': 'Tom', 'lname': 'David', 'email': 'tom.david@example.com', 'age': 'thirty-one'}