"*** Python Basics - Final Project: Student Management"
"*** Module Name:  main.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-07-18"
"*** Notes:  Entry point of the student management system. Wires together the objects and runs the menu loop."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"

from actions import StudentManager
from data import CsvStudentRepository
from menu import Menu


class StudentApp:
    """Builds the manager and the menu, then runs until the user exits."""

    def __init__(self):
        self.running = True
        self.manager = StudentManager(CsvStudentRepository())
        self.menu = Menu("Lyfter Students Califications Records", [
            ("Register a new student", self.manager.register_students),
            ("Show all students", self.manager.show_students),
            ("Show Top 3 students", self.manager.show_top_3),
            ("Show overall average", self.manager.show_average),
            ("Show failed students", self.manager.show_failed_students),
            ("Delete a student", self.manager.delete_student),
            ("Export data to CSV", self.manager.export_data),
            ("Import data from CSV", self.manager.import_data),
            ("Exit", self.exit),
        ])

    def exit(self):
        print("\n Logging out and exiting...")
        self.running = False

    def run(self):
        while self.running:
            action = self.menu.choose()
            action()


if __name__ == "__main__":
    StudentApp().run()
