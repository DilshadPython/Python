"""
Demonstrates differences between object attribute deletion (delattr / del obj.attr)
and dictionary key deletion (del dict[key]).
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Dict


class CarProfile:
    """Class representing car specifications."""
    def __init__(self, brand: str = "Audi", year: int = 2005, model: str = "A3"):
        self.brand: str = brand
        self.year: int = year
        self.model: str = model


def delete_object_attribute(car_obj: CarProfile, attr_name: str) -> bool:
    """Delete an attribute from a object instance using delattr."""
    if hasattr(car_obj, attr_name):
        delattr(car_obj, attr_name)
        return True
    return False


def delete_dictionary_key(car_dict: Dict[str, Any], key_name: str) -> bool:
    """Delete a key from a dictionary using del dict[key]."""
    if key_name in car_dict:
        del car_dict[key_name]
        return True
    return False


if __name__ == '__main__':
    car = CarProfile("Audi", 2005, "A3")
    print("Car instance dict:", car.__dict__)
    delete_object_attribute(car, "year")
    print("Car instance after delattr('year'):", car.__dict__)

    car_data: Dict[str, Any] = {"brand": "Volvo", "year": 2010, "model": "EX90"}
    print("Car dict before:", car_data)
    delete_dictionary_key(car_data, "year")
    print("Car dict after del dict['year']:", car_data)
