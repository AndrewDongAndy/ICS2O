

class Course:

    """A blueprint for a school course. Helps teachers
    keep track of the students and their progress."""

    version = '0.2'

    def __init__(self, code, teacher, room, students=None, weights=None):
        """Records the course code, teacher name, room number,
        student objects, and evaluation weights."""
        self.code = code
        self.teacher = teacher
        self.room = room

        # Note: avoid passing in mutable data types
        if students is None:
            self.students = []
        else:
            self.students = students

        if weights is None:
            # Default weights shown below
            self.weights = {
                'K': 0.175,
                'A': 0.175,
                'T': 0.175,
                'C': 0.175,
                'final summative': 0.1,
                'final exam': 0.2
            }
        else:
            self.weights = weights

    def add_student(self, student):
        """Adds a student (object) to the list
        of students for this course."""
        if student not in self.students:
            self.students.append(student)
            student.add_course(self)

    def add_mark(self, student, field, mark):
        """Adds the mark in the given field
        to this Course of the student."""
        if student in self.students:
            student.add_mark(self, field, mark)


class Student:

    """The one-stop shop for teachers to keep track of students'
    marks. Your personalized advanced toolkit."""

    version = '0.1'

    def __init__(self, first, last, oen, courses=None):
        """Records first and last names, oen number,
        and Courses (objects) enrolled in a list."""
        self.first = first
        self.last = last
        self.oen = oen

        self.marks = {}

        # As above, don't pass in mutable data types
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
            for course in courses:
                course.add_student(self)

            for course in courses:
                self.marks[course.code] = {}
                for field in course.weights:
                    scores[course.code][field] = []

    def add_course(self, course):
        """Adds a course (object) to the student."""
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

        self.marks[course.code] = {}
        for field in course.weights:
            self.marks[course.code][field] = []

    @staticmethod
    def is_school_day(date):
        """Returns True if the date is a weekday, otherwise returns False."""
        if date.weekday() == 5 or date.weekday() == 6:
            return True
        return False

    @classmethod
    def from_string(cls, string):
        """Returns an instance of Student from
        a string of the form first-last-oen."""
        first, last, oen = string.split('-')
        return cls(first, last, oen)

    @property
    def fullname(self):
        """Returns the full name of the Student."""
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        """Allows setting the full name of a Student (object)."""
        first, last = name.split()
        self.first = first
        self.last = last

    @property
    def email(self):
        """Returns the email address of the Student."""
        return '{}{}{}@ugcloud.ca'.format(self.first[:2], self.last[:3], self.oen[-4:])

    def add_mark(self, course, field, mark):
        """Adds the given mark to the corresponding field
        in the course specified."""
        if field in course.weights:
            self.marks[course.code][field].append(mark)

    @staticmethod
    def average(nums):
        """Returns the arithmetic mean of a list of numbers;
        returns 0 if the list is empty."""
        if len(nums) > 0:
            return sum(nums) / len(nums)
        return 0

    def overall_mark(self, course):
        avg = 0
        for field, weight in course.weights.items():
            field_marks = self.marks[course.code][field]
            avg += Student.average(field_marks) * weight
        return avg


# Code for testing - works!
CS = Course('ICS2O', 'Schaeffer', 'C206')
Andy = Student('Andy', 'Dong', '12345')

Andy.add_course(CS)
for student in CS.students:
    print(student.fullname)

Kevin = Student.from_string('Kevin-Dong-98765')
CS.add_student(Kevin)
for course in Kevin.courses:
    print(course.code)
print(Kevin.oen)
print(Kevin.marks)
CS.add_mark(Kevin, field='C', mark=80)
CS.add_mark(Kevin, field='C', mark=80)
CS.add_mark(Kevin, field='T', mark=80)
CS.add_mark(Kevin, field='T', mark=80)
CS.add_mark(Kevin, field='T', mark=80)
CS.add_mark(Kevin, field='A', mark=80)
CS.add_mark(Kevin, field='K', mark=80)
CS.add_mark(Kevin, field='T', mark=80)
CS.add_mark(Kevin, field='final summative', mark=80)
CS.add_mark(Kevin, field='final exam', mark=80)
print(Kevin.marks)
print(Kevin.overall_mark(CS))
