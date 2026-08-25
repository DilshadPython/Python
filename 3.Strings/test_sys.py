"""
Interpreter Information and Object Property Formatting (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `@property` decorator exposes computed attributes.
  `sys.executable` and `sys.version` return path and version string of the active interpreter.
"""

from __future__ import print_function
import sys


class Employee(object):
    """Represents an employee with dynamic string property formatting."""

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def test_function(self):
        """Placeholder method for testing."""
        pass

    @property
    def email(self):
        """Formats employee email address."""
        return '{0}.{1}@gmail.com'.format(self.firstname, self.lastname)

    @property
    def full_name(self):
        """Formats full name string."""
        return '{0} {1}'.format(self.firstname, self.lastname)


def get_sys_info():
    """Returns current interpreter executable path and version."""
    return {
        "executable": sys.executable,
        "version": sys.version
    }


def main():
    """Demonstrates sys info and Employee property formatting."""
    info = get_sys_info()
    print("Executable:", info["executable"])
    print("Version:", info["version"])

    emp = Employee('Dilshad', 'Abdulla')
    print("Email:", emp.email)
    print("Full Name:", emp.full_name)
    return emp


if __name__ == '__main__':
    main()

