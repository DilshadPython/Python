from pydantic import validate_call


@validate_call
def user_detail(fname: str, lname: str, age: int) -> dict:
    email = f"{fname.lower()}.{lname.lower()}@example.com"
    
    '''
    Using python check up for type hints instead of using mypy this is manual type checking
    '''
    # if not isinstance(fname, str):
    #     raise TypeError("First name must be a string")
    # if not isinstance(lname, str):
    #     raise TypeError("Last name must be a string")
    # if not isinstance(age, int):
    #     raise TypeError("Age must be an integer")
    
    return {
        'fname': fname,
        'lname': lname,
        'email': email,
        'age': age,
    }
    
user = user_detail("Jane", "Doe", 28)
print(user)

# if you want to use validate?_call make this line uncommented to see the error
# first_user = user_detail("Tom", "David", "thirty-one")
# print(first_user)