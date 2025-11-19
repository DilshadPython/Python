To install Mypy in VScode use following:
python3 -m pip install mypy

To use it with your file code run:
mypy example.py Not python example.py

type User = dict[str, str | int | RGB | None]

Next:

def create_user(fname: str, lname: str, age: int | None = None) -> dict[str, str | int | None]:
or


Change it to:

def create_user(fname: str, lname: str, age: int | None = None) -> User:


to create new color using:
type RBG = tuple[int, int, int]
    
    or

type HSL = tuple[int, int, int]

To make it easier we use third party package called typing:

from typing import Newtype

Next the color ailians will change to

type RGB = tuple[int, int, int] change it TO:

type User = dict[str, str | int | RGB | None, HSL | None]


RGB = NewType("RGB", tuple[int, int, int])

type HSL = tuple[int, int, int]

HSL = NewType("HSL", tuple[int, int, int])

Next we will change :

def create_user(fname: str, lname: str, age: int | None = None, ch_color: RGB | None = None, fav_color: HSL | None = None) -> User:

first_user = create_user("john", "Smith", 30, ch_color=(27, 204, 187))
To:
first_user = create_user("john", "Smith", 30, ch_color=RGB((27, 204, 187)))
second_user = create_user("Alice", "George", 37, ch_color=HSL((255, 97, 185)))

Next we will define another age as str where age is an integer but it still working because we have str in the definition of union

We import TypedDict after we import NewType

Next we create class inherit from TypedDict make the code much easier to understand

We change: type User = dict[str, str | int | RGB | None, HSL | None]

To:

class User(TypedDict):
    first_name: str

Next Remove:
age_str: str(age)

# We remove TypedDict and changed to dataclass
Change:  class User(TypedDict):

To:
@dataclass
class User:

Next we change:

 return User(
        "fname": fname,
        "lname": lname,
        "email": email,
        "age": age,
        "ch_color": ch_color,
        "fav_color": fav_color,
    )

To:
return User(
    fname=fname,
    lname=lname,
    email=email,
    age=age,
    ch_color=ch_color,
    fav_color=fav_color,
)