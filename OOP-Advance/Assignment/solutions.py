import os


class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fn:
                for line in fn:
                    line = line.rstrip()  # remove the right whitespace
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fn:
        	# items() is a statment return two items 
            for key, value in self.items():
                fn.write('{0}={1}\n'.format(key, value))


obj = ConfigDict('config.txt')

obj['key'] = 'value'
