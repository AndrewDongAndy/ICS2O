

class Course:

    """A blueprint for a school course. Helps teachers
    keep track of the students and their progress."""

    version = '0.2'
    all_courses = []

    def __init__(self, id, teacher, room, students=None, weights=None):
        """Records the course id, teacher name, room number,
        student objects, and evaluation weights."""
        Course.all_courses.append(self)
        self.id = id
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

    def add_mark(self, student, field, mark, desc):
        """Adds the mark in the given field
        to this Course of the student."""
        if student in self.students:
            student.add_mark(self, field, mark, desc)


class Student:

    """The one-stop shop for teachers to keep track of students'
    marks. Your personalized advanced toolkit."""

    version = '0.1'
    all_students = []

    def __init__(self, first, last, oen, courses=None):
        """Records first and last names, oen number,
        and Courses (objects) enrolled in a list."""
        Student.all_students.append(self)
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
                self.marks[course.id] = {}
                for field in course.weights:
                    scores[course.id][field] = {}

    def add_course(self, course):
        """Adds a course (object) to the student."""
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

        self.marks[course.id] = {}
        for field in course.weights:
            self.marks[course.id][field] = []

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

    def add_mark(self, course, field, mark, desc):
        """Adds the given mark to the corresponding field
        in the course specified."""
        if field in course.weights:
            self.marks[course.id][field][desc] = mark

    @staticmethod
    def is_school_day(date):
        """Returns True if the date is a weekday, otherwise returns False."""
        if date.weekday() == 5 or date.weekday() == 6:
            return True
        return False

    @staticmethod
    def average(nums):
        """Returns the arithmetic mean of a list of numbers;
        returns 0 if the list is empty."""
        if len(nums) > 0:
            return sum(nums) / len(nums)
        return 0

    @staticmethod
    def letter_grade(mark):
        """Returns the letter grade, uses the Canadian grading system;
        retrieved from https://en.wikipedia.org/wiki/Academic_grading_in_Canada"""
        if 89 <= mark <= 100:
            return 'A+'
        elif 85 <= mark < 89:
            return 'A'
        elif 80 <= mark < 85:
            return 'A-'
        elif 77 <= mark < 80:
            return 'B+'
        elif 73 <= mark < 77:
            return 'B'
        elif 70 <= mark < 73:
            return 'B-'
        elif 67 <= mark < 69:
            return 'C+'
        elif 63 <= mark < 67:
            return 'C'
        elif 60 <= mark < 63:
            return 'C-'
        elif 55 <= mark < 60:
            return 'D+'
        elif 50 <= mark < 55:
            return 'D'
        else:
            return 'F'

    def overall_mark(self, course):
        avg = 0
        for field, weight in course.weights.items():
            field_marks = self.marks[course.id][field].values
            avg += Student.average(field_marks) * weight
        return avg

    def print_overview(self):
        for course in self.courses:
            print('{} - {}, {}'.format(course.id, course.teacher, course.room))
            for field, scores in self.marks[course.id].items():
                print(field + ':', scores)


class Teacher:

    all_teachers = []

    def __init__(self, first, last, courses=None):
        self.first = first
        self.last = last

        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


'''
# Code for testing - works!
CS = Course('ICS2O', 'Schaeffer', 'C206')
Andy = Student('Andy', 'Dong', '12345')

Andy.add_course(CS)
for student in CS.students:
    print(student.fullname)

Kevin = Student.from_string('Kevin-Dong-98765')
CS.add_student(Kevin)
for course in Kevin.courses:
    print(course.id)
print(Kevin.oen)
print(Kevin.marks)
CS.add_mark(Kevin, field='C', mark=80, desc='Unit 1')
CS.add_mark(Kevin, field='C', mark=80, desc='Unit 2')
CS.add_mark(Kevin, field='T', mark=80, desc='Unit 4')
CS.add_mark(Kevin, field='T', mark=80, desc='Unit 3')
CS.add_mark(Kevin, field='T', mark=80, desc='Unit 6')
CS.add_mark(Kevin, field='A', mark=80, desc='Unit 7')
CS.add_mark(Kevin, field='K', mark=80, desc='Unit 14')
CS.add_mark(Kevin, field='T', mark=80, desc='Unit 1')
CS.add_mark(Kevin, field='final summative', mark=80, desc='Unit 1')
CS.add_mark(Kevin, field='final exam', mark=80, desc='Unit 1')
print(Kevin.marks)
print(Kevin.overall_mark(CS))
Kevin.print_overview()
'''

Andy = Student('Andy', 'Dong', '12345')
CS = Course('ICS2O', 'Schaeffer', 'C206')
CS.add_student(Andy)
Schaeffer = Teacher('Eben', 'Schaeffer', [CS])

for student in Student.all_students:
    with open(student.oen + '.txt', 'w') as f:
        f.write(Andy.fullname + ', ' + Andy.oen)
        for course in Andy.courses:
            f.write('\n' + 'Overview for ' + course.id + ':')

for course in Schaeffer.courses:
    with open(course.id + '.txt', 'w') as f:
        f.write()
        f.write('\n' + 'Overview for ' + course.id)
