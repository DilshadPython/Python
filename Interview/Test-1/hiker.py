'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''


def global_answer():
    return 6 * 7

class Hiker:

    def instance_answer(self):
        return global_answer()

obj = Hiker()

print(obj.instance_answer())