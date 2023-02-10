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