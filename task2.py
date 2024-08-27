class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self, subject=None):
        if subject:
            grades = self.grades.get(subject, [])
            return sum(grades) / len(grades) if grades else 0
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_grades(self):
        for subject, grades in self.grades.items():
            average = self.calculate_average(subject)
            letter_grade = self.get_letter_grade(average)
            gpa = self.get_gpa(average)
            print(f"Subject: {subject}")
            print(f"Grades: {grades}")
            print(f"Average: {average:.2f}")
            print(f"Letter Grade: {letter_grade}")
            print(f"GPA: {gpa:.2f}")
            print("------------------------")

def main():
    grades = StudentGrades()
    while True:
        print("1. Add Grade")
        print("2. Calculate Average")
        print("3. Display Grades")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            grades.add_grade(subject, grade)
        elif choice == "2":
            subject = input("Enter subject (or leave blank for overall): ")
            if subject:
                average = grades.calculate_average(subject)
                print(f"Average for {subject}: {average:.2f}")
            else:
                average = grades.calculate_average()
                print(f"Overall Average: {average:.2f}")
        elif choice == "3":
            grades.display_grades()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()