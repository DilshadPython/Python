# must be inherite from dict built-in methods
class DoThis():

    def __setitem__(self, key, val):

        # Don't use this because become recursive loops or func call itself
        # self[key] = vale
        # this way avoid recursive function or loops
        dict.__setitem__(self, key, val)


obj = DoThis()

obj['key'] = 'val'
