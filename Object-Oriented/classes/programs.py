
class Program():

    def __init__(self, *args, **kwargs):
        self.language = input('Enter tha lang: ')
        self.version = float(input('Enter the version: '))
        self.skill = input('Enter skills level: ')

    def upgrade_version(self):
        new_version = float(input('Update your version: '))
        print('You have updated the ', self.language, self.version, ' version to the ',
              self.language, new_version)
        self.version = new_version

obj = Program()

obj.upgrade_version()
