Regular Method:
Regular method use self as first argument

Class method:
Class method use cls as first argument

Static Method:
static method not use anyof self or cls as first argument.

The 6 important Points to understanding Classes
1. Instance knows which class come it from.
2. Variables are define in the class are available to the instance.
3. A method on an instance passes instance as the first amount to the method
	(renamed self in the method)
4. Instances have their own data, instance attributes
5. Variables defined in the class are called class attributes
6. When we read an attribute, Python looks for it first in the instance, and then the class.