

def create_username(username, email, age):
    if not isinstance(username, str):
        raise TypeError("Username must be a non-empty string.")
    if not isinstance(email, str):
        # if "@" not in email or "." not in email.split("@")[-1]:
        raise TypeError("Email must be a valid email address include format.")
    if not isinstance(age, int) or age < 0:
        raise TypeError("Age must be a non-negative integer.")
    
    return {
        "username": username,
        "email": email,
        "age": age
    }

first_user = create_username("john", "john@gmail.com", 30)
print(first_user)

second_user = create_username("alice", "dilshad.a73@gmail.com", 37)
print(second_user)

