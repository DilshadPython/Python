https://docs.python.org/3/library/argparse.html
The argparse module makes it easy to write user-friendly command-line interfaces.
The program defines what arguments it requires, and argparse will figure out how to parse
those out of sys.argv. The argparse module also automatically generates help and usage messages.
The module will also issue errors when users give the program invalid arguments.


 py example.py -h
usage: example.py [-h] [-n N]

options:
  -h, --help  show this help message and exit
  -n N

@ py sample.py -h -n
usage: sample.py [-h] [-n N]

Argument Parser Messages in print

options:
  -h, --help  show this help message and exit
  -n N


/Python/Argparse$ py argpars.py  -h
usage: ProgramName [-h] [-c COUNT] [-v] filename

What the program does

positional arguments:
  filename

options:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
  -v, --verbose

Text at the bottom of help


@Argparse$ py exam.py
Messages
py exam.py 3
usage: exam.py [-h] [-n N]
exam.py: error: unrecognized arguments: 3
