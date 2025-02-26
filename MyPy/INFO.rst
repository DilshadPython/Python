to install mypy

https://mypy.readthedocs.io/en/stable/getting_started.html#installing-and-running-mypy

python3 -m pip install mypy

The outcome is like that:

error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

# To resolve the issue you have to install python3-xyz where xyz is the package you are trying to install

pip3 install --break-system-packages mypy

# testing example.py
py example.py
Enter a number: 4
Traceback (most recent call last):
  File "/home/MyPy/example.py", line 14, in <module>
    number(num)
  File "/home/MyPy/example.py", line 8, in number
    for _ in range(n):
             ^^^^^^^^
TypeError: 'str' object cannot be interpreted as an integer

to resolve the issue it should be int(input('Enter an num: '))
mypy example.py
Success: no issues found in 1 source file
/MyPy$ py example.py
Enter a number: 9
Hello Python mypy
Hello Python mypy
Hello Python mypy
Hello Python mypy
Hello Python mypy
Hello Python mypy
Hello Python mypy
Hello Python mypy
Hello Python mypy

