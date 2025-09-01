"""
OOP Mini Project Number 2
Category: Core OOP Concepts

2.	Design a Student and Course class with enrollment logic.

Problem Statement:
------------------
Design a Student and Course class with enrollment logic.

Requirements:
-------------
1. Create a Student class that stores:
   - name
   - student ID
   - courses the student is enrolled in

2. Create a Course class that stores:
   - course name
   - course code
   - list of enrolled students

3. A student should be able to enroll in multiple courses.
4. A course should keep track of multiple students.
5. We should be able to:
   - Show all courses a student is enrolled in.
   - Show all students enrolled in a course.

Concepts Demonstrated:
----------------------
- Classes and Objects (OOP fundamentals)
- Encapsulation (storing student & course details safely)
- Object Relationships (Student ↔ Course link each other)
"""

class Course:
    def __init__(self, course_name, course_code):
        """Initialize a course with name and code"""
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []  # list of Student objects

    def add_student(self, student):
        """Enroll a student in this course"""
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f" Student {student.name} enrolled in {self.course_name}")
        else:
            print(f" Student {student.name} is already enrolled in {self.course_name}")

    def show_students(self):
        """Display all students enrolled in this course"""
        if self.enrolled_students:
            print(f"\n📘 Students in {self.course_name}:")
            for s in self.enrolled_students:
                print(f"- {s.name} (ID: {s.student_id})")
        else:
            print(f"\n No students enrolled in {self.course_name}")


class Student:
    def __init__(self, name, student_id):
        """Initialize student with name and ID"""
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []  # list of Course objects

    def enroll(self, course):
        """Enroll this student in a course"""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)
        else:
            print(f" {self.name} is already enrolled in {course.course_name}")

    def show_courses(self):
        """Display all courses this student is enrolled in"""
        if self.enrolled_courses:
            print(f"\n👨‍🎓 {self.name} (ID: {self.student_id}) is enrolled in:")
            for c in self.enrolled_courses:
                print(f"- {c.course_name} ({c.course_code})")
        else:
            print(f"\n{self.name} is not enrolled in any course yet")


# ============================================================
# Main Program (Testing the Classes)
# ============================================================

if __name__ == "__main__":
    # Create courses
    math = Course("Mathematics", "MATH101")
    physics = Course("Physics", "PHYS201")

    # Create students
    student1 = Student("Yasir", "Y007")
    student2 = Student("Abdullah", "A007")

    # Enroll students in courses
    student1.enroll(math)
    student1.enroll(physics)
    student2.enroll(math)

    # Trying duplicate enrollment
    student1.enroll(math)

    # Show courses for each student
    student1.show_courses()
    student2.show_courses()

    # Show students in each course
    math.show_students()
    physics.show_students()

# ============================================================
# Sample Output:
# ============================================================
#  Student Yasir enrolled in Mathematics
#  Student Yasir enrolled in Physics
#  Student Abdullah enrolled in Mathematics
#  Student Yasir is already enrolled in Mathematics
#
#  Yasir (ID: Y007) is enrolled in:
# - Mathematics (MATH101)
# - Physics (PHYS201)
#
#  Abdullah (ID: A007) is enrolled in:
# - Mathematics (MATH101)
#
#  Students in Mathematics:
# - Yasir (ID: Y007)
# - Abdullah (ID: A007)
#
#  Students in Physics:
# - Yasir (ID: Y007)
# ============================================================
