import cowsay
import sys


if len(sys.argv) == 2:
    cowsay.cow('Hello I am a, ' + sys.argv[1])
