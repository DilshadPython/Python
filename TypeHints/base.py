
"""
# from typing import Optional, Dict, Any
installed mypy type checker in python to check the code before runing

def create_user(fname: str, lname: str, age: Optional[int] = None) -> Dict[str, Any]:

added -> dict to indicate the return type of the function
because age is an integer and optional, we can use None as default value we use union type | to indicate that age can be either int or None

we change the function to type ailias
def create_user(fname: str, lname: str, age: int | None = None) -> dict[str, str | int | None]:

type User = dict[str, str | int | None]

for tupe alias (RGB stand for colour red green blue)

type RGB = tuple[int, int, int]
type HSL = tuple[int, int, int]
"""
from typing import NewType  #, TypedDict
from dataclasses import dataclass

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# type User = dict[str, str | int | RGB | None, HSL | None]
# class User(TypedDict):

@dataclass
class User:
    fname: str
    lname: str
    email: str
    age: int | None = None
    ch_color: RGB | None = None
    fav_color: HSL | None = None
    

def create_user(fname: str, lname: str, age: int | None = None, ch_color: RGB | None = None, fav_color: HSL | None = None) -> User:
    email = f"{fname.lower()}.{lname.lower()}@example.com"

    
    return User(
        fname=fname,
        lname=lname,
        email=email,
        age=age,
        ch_color=ch_color,
        fav_color=fav_color,
    )

first_user = create_user("john", "Smith", 30, ch_color=RGB((27, 204, 187)))
print(first_user)

second_user = create_user("Alice", "George", 37, fav_color=HSL((255, 97, 185)))
print(second_user)

# I put age as str to see if the VScode showing error automatically
# third_user = create_user("Alice", "George", '37', fav_color=HSL((255, 97, 185)))
# print(third_user)