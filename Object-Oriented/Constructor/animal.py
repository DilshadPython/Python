# class with initialization __init__
# The double underscorr signified for private or magic because it use internally
# It is not called by the user in the class it's called automatically
class Animal:

    def __init__(self, name, sound):
        print('Call automatically __init__')
        self.name = name
        self.sound = sound

    def sound_say(self):
        if self.name == 'Dog':
            print('The {} sound is bagging'.format(self.name))
        elif self.name == 'Cat':
            print('The {} sound is miaw'.format(self.name))

# Animal(name_required, sound_required)
# As soon instance obj (dogy or caty) called soun_say() method call __init__ automatically


dogy = Animal('Dog', 'bugging')
caty = Animal('Cat', 'miawing')

dogy.sound_say()

caty.sound_say()
