class Student:
    # grade cutoffs - top to bottom
    GRADE_RULES = [
        (80, "A"),
        (70, "B"),
        (60, "C"),
        (50, "D")
    ]

    def __init__(self, name, marks):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty.")

        # bool is a subclass of int, so we check it separately
        if isinstance(marks, bool) or not isinstance(marks, (int, float)):
            raise TypeError("Marks must be a number.")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.name = name.strip()

        # show 85 instead of 85.0
        self.marks = int(marks) if marks == int(marks) else marks

    def get_grade(self):
        for cutoff, grade in self.GRADE_RULES:
            if self.marks >= cutoff:
                return grade
        return "Fail"

    def display_result(self):
        print()
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")

    def __str__(self):
        return f"{self.name} ({self.marks}, Grade: {self.get_grade()})"


if __name__ == "__main__":
    students = []

    while True:
        name = input("\nEnter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        try:
            marks = float(input("Enter marks (0 to 100): "))
            student = Student(name, marks)
            students.append(student)
            print("Student added successfully!")
        except (ValueError, TypeError) as error:
            print(f"Invalid input: {error}")
            continue

        choice = input("Add another student? (yes/no): ").strip().lower()
        if choice != "yes":
            break

    print("\n===== STUDENT RESULTS =====")

    for student in students:
        student.display_result()
        print("-" * 25)