class Student:
    def __init__(self, marks):
        self._marks = marks   # underscore means internal variable

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks!")

s = Student(85)
print(s.marks)

s.marks = 110   # Invalid
s.marks = 95    # Valid
print(s.marks)
