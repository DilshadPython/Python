The relationships betwwen Class Attribute and Instance Attribute
1. Attributes/Variables in the class are accessible through the instance object created
	of the current class has been define
2. Instance Attribute as well accessible by the instance object
3. When we use syntax object.attribute, we're asking python to look up the attribute
	- First in the instance
	- Then in the class
4. Method calls through the instance follow this lookup

The 6 important Points to understanding Classes
1. Instance knows which class come it from.
2. Variables are define in the class are available to the instance.
3. A method on an instance passes instance as the first kwrg to the method
	(renamed self in the method)
4. Instances have their own data, instance attributes
5. Variables defined in the class are called class attributes
6. When we read an attribute, Python looks for it first in the instance, and then the class.