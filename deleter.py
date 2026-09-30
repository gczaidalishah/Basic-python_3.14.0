class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

s = Student("Ali")
del s.name
print(s.name)  # This will raise an AttributeError because the name attribute has been deleted.