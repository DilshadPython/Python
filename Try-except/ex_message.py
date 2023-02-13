class SomeError(Exception):

    # *args is mean accept any argument any number of args
    def __init__(self, *args):
        print('Calling int')
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('Calling str')
        if self.message:
            return "Here's a SomeError exception with message: {0}".format(self.message)
        else:
            return "Here's a SomeError Exception"


# here we call without any args
raise SomeError

# here we call with an args
raise SomeError("Hey, we have a problem!")
