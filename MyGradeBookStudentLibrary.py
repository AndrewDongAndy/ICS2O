

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
        """Removes a student (object) from the list
        of students for this course."""
        if student not in self.students:
            self.students.append(student)

    def record_grade(self, student, field, desc, grade):
        student_index = self.students.index(student)
        self.students[student_index].



class Student:

    """The one-stop shop for teachers to keep track of students'
    grades. Your personalized advanced toolkit."""

    version = '0.1'

    def __init__(self, first, last, oen, courses=None):
        """Records first and last names, oen number,
        and courses enrolled."""
        self.first = first
        self.last = last
        self.oen = oen

        # As above, don't pass in mutable data types
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def new_course(self, course):
        """Adds a course (object) to the student."""
        self.courses.append(course)

    @staticmethod
    def is_school_day(date):
        """Returns True if the date is a weekday, otherwise returns False."""
        if date.weekday() == 5 or date.weekday() == 6:
            return True
        return False

    @classmethod
    def from_string(cls, string):
        """Returns an instance of MyGradeBook from
        a string of the form first-last-oen."""
        first, last, oen = string.split()
        return cls(first, last, oen)
