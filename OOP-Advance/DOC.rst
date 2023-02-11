@property
Is a decorator that designates an instance attribute as encapsulate-able throuhh methods

Getter, setter and deleting methods can be defined, called automatically when a user accesses the attribute

The names are linked to the attribute name-the methods, and setter and deleter methods must use it.

@property offers some control, but don't try to force the user into creatin behaviors-it's un-Pythonic

@property should not encapsulate expensive operation, because attribute setting looks cheap!

@property controls attribute that are expected, but can't control attributes that are unexpected.

__slots__ can define allowable attributes
 - Saves memory by defining attributes ahead of the time
 - Should not be used to limit attribute - unPythonic!

 # PEP8 stand for Python Enhancement Proposal 8, or PEP 8, is a style guide for Python code. In 2001, Guido van Rossum, Barry Warsaw, and Nick Coghlan created PEP 8 to help Python programmers write consistent and readable code.

 PEP8 rules:
 - Module names: all lower case (file_name.py)
 - Class names and exception name CarName
 - Globals and locals: all lower case 
 - Functions and methods all lower case. def car_name():
 - Constants: ALL CAPS or all upper case

 Public and Private Variable nameing:
 - Public attribute or variables (intended to be use by the importer of this module or user of the class): regular lower case
 - Private attribute or variables (intended to be use by the importer of this module or user of the class): _single leading underscore
 - Private attribute's that shouldn't be subclassed: __double leading underscore
 - Magic attributes: __double_underscore (use them, don't create them) 

 # Style of old and new classes
 - Inherit from 'object'
 - Can be constructed with default attribute form 'metaclass' constructors
 - Allow the subclassing of built-ins
 - Allow the use of 'slots' define instance attributes
 - Use the 'C3' MRO (method resolution order)
 - Support 'descriptors'
 - Are the only style of class in Python3