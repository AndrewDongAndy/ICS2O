from datetime import datetime


class MyGradeBookStudent:

    '''The one-stop shop for teachers to keep track of students'
    grades. Your personalized advanced toolkit.'''

    version = '0.1'

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.courses = {}

    def new_course(self, course_code):
        "Adds a course to the student."
        self.courses[course_code] = {}

    def input_score(course_name, score):
        pass

    @staticmethod
    def isschoolday(date):
        "Returns True if the date is a weekday, otherwise returns False."
        if date.weekday in [5, 6]:
            return True
        return False

    @classmethod
    def fromfullname(cls, fullname):
        "Returns an instance of MyGradeBook from a fullname."
        first, last = fullname.split()
        return cls(first, last)
