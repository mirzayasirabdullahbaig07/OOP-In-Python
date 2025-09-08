"""
Project: Student Grade Analyzer
Field: Education / Data Analysis
Concepts Used: OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)
"""

from abc import ABC, abstractmethod
from statistics import mean


class Person(ABC):
    """
    Person Class (Abstract Base Class):
    -----------------------------------
    - Base class for all persons (students, teachers, etc.).
    - Defines common attributes like name and ID.
    """

    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id

    @abstractmethod
    def display_info(self):
        """Abstract method to display person details."""
        pass


class Student(Person):
    """
    Student Class:
    --------------
    - Inherits from Person.
    - Stores subject marks and provides methods for analysis.
    """

    def __init__(self, name: str, student_id: int):
        super().__init__(name, student_id)
        self.marks = {}

    def add_mark(self, subject: str, score: float):
        """Add or update marks for a subject."""
        self.marks[subject] = score

    def calculate_average(self) -> float:
        """Calculate average marks."""
        return mean(self.marks.values()) if self.marks else 0.0

    def get_grade(self) -> str:
        """Assign grade based on average marks."""
        avg = self.calculate_average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    def display_info(self):
        """Display student details and marks."""
        print(f"👨‍🎓 {self.name} (ID: {self.student_id})")
        for subject, score in self.marks.items():
            print(f"   📘 {subject}: {score}")
        print(f"   📊 Average: {self.calculate_average():.2f}, Grade: {self.get_grade()}\n")


class GradeAnalyzer:
    """
    GradeAnalyzer Class:
    --------------------
    - Manages multiple students.
    - Provides insights like top performer, class average, and weakest student.
    """

    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        """Add a student to the analyzer."""
        self.students.append(student)

    def show_all_students(self):
        """Display info for all students."""
        for student in self.students:
            student.display_info()

    def class_average(self) -> float:
        """Calculate overall class average."""
        if not self.students:
            return 0.0
        return mean([s.calculate_average() for s in self.students])

    def top_student(self) -> Student:
        """Find the student with the highest average."""
        return max(self.students, key=lambda s: s.calculate_average(), default=None)

    def weakest_student(self) -> Student:
        """Find the student with the lowest average."""
        return min(self.students, key=lambda s: s.calculate_average(), default=None)


# ------------------ Example Usage ------------------ #
if __name__ == "__main__":
    analyzer = GradeAnalyzer()

    # Create students
    s1 = Student("Ali", 101)
    s2 = Student("Fatima", 102)
    s3 = Student("Hassan", 103)

    # Add marks
    s1.add_mark("Math", 90)
    s1.add_mark("Science", 80)

    s2.add_mark("Math", 60)
    s2.add_mark("Science", 65)

    s3.add_mark("Math", 40)
    s3.add_mark("Science", 50)

    # Add students to analyzer
    analyzer.add_student(s1)
    analyzer.add_student(s2)
    analyzer.add_student(s3)

    # Show details
    print("📋 Student Records:\n")
    analyzer.show_all_students()

    # Class insights
    print(" Class Analysis:")
    print(f" Class Average: {analyzer.class_average():.2f}")
    print(f" Top Student: {analyzer.top_student().name}")
    print(f" Weakest Student: {analyzer.weakest_student().name}")
