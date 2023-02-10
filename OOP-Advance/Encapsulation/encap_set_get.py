class Monitor:
    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value


obj1 = Monitor()
obj2 = Monitor()

obj1.set_val(22)
obj2.set_val(55)

print(obj1.get_val())
print(obj2.get_val())
