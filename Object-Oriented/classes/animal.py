# class with initialization __init__
class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def sound_say(self):
        if self.name == 'Dog':
            print('The {} sound is bagging'.format(self.name))
        elif self.name == 'Cat':
            print('The {} sound is miaw'.format(self.name))

# Animal(name_required, sound_required)

dogy = Animal('Dog', 'bugging')
caty = Animal('Cat', 'miawing')

dogy.sound_say()

caty.sound_say()
