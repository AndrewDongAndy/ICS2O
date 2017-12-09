class Mark:

    all_marks = []

    def __init__(self, student, course, mark, desc=None):
        Mark.all_marks.append(self)

        self.student = student
        self.course = course
        self.mark = mark

        if desc is None:
            self.desc = 'No description'
        else:
            self.desc = desc

    def __del__(self):
        print('Deleted instance')
        Mark.all_marks.remove(self)


print(len(Mark.all_marks))
mark1 = Mark('Andy', 'ICS2O', 99, 'Intro to Computers Test')
print(len(Mark.all_marks))

mark1.__del__()
print(len(Mark.all_marks))
