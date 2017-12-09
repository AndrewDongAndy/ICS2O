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


mark1 = Mark('Andy', 'ICS2O', 99, 'Intro to Computers Test')
for mark in Mark.all_marks:
    print(mark.student, mark.course)
del mark1
print(len(Mark.all_marks))
