"*** Python Intermediate - Refactory of Project: Student Management using OOP"
"*** Module Name:  actions.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2026-11-15"
"*** Notes:  Defines the StudentManager class, which owns the list of students and all the actions on it."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"

from student import Student


class StudentManager:
    """Keeps the students and provides every action the menu offers."""

    def __init__(self, repository):
        self._students = []
        self._repository = repository

    # ---------- Core operations (no input/print) ----------

    def exists(self, student: Student) -> bool:
        return student in self._students

    def find(self, nombre: str, seccion: str):
        """Returns the matching Student or None."""
        for student in self._students:
            if student.nombre.lower() == nombre.strip().lower() and student.seccion == seccion.strip().upper():
                return student
        return None

    def add(self, student: Student):
        if self.exists(student):
            raise ValueError(f"The student '{student.nombre}' is already registered in section '{student.seccion}'.")
        self._students.append(student)

    def remove(self, student: Student):
        self._students.remove(student)

    def top(self, amount: int = 3) -> list:
        return sorted(self._students, key=lambda s: s.average, reverse=True)[:amount]

    def general_average(self) -> float:
        return sum(s.average for s in self._students) / len(self._students)

    def failed_students(self) -> list:
        return [s for s in self._students if s.has_failed()]

    # ---------- Input helpers ----------

    @staticmethod
    def _ask(prompt: str, validator):
        """Asks until the validator accepts the input."""
        while True:
            try:
                return validator(input(prompt))
            except ValueError as error:
                print(f" {error}")

    @staticmethod
    def _ask_yes_no(prompt: str) -> bool:
        return input(prompt).strip().lower() == "y"

    # ---------- Menu actions ----------

    def register_students(self):
        """Allows the entry of multiple students one at a time."""
        while True:
            print("\n--- New Student Record ---")
            nombre = self._ask("Full Name: ", Student.validate_name)
            seccion = self._ask("Section (e.g., 11B): ", Student.validate_section)

            if self.find(nombre, seccion):
                print(f" The student '{nombre}' is already registered in section '{seccion}'.")
                if not self._ask_yes_no("Do you want to try with another student? (y/n): "):
                    break
                continue

            espanol = self._ask("Ingrese la nota de Español (0-100): ", Student.validate_score)
            ingles = self._ask("Ingrese la nota de Inglés (0-100): ", Student.validate_score)
            sociales = self._ask("Ingrese la nota de Sociales (0-100): ", Student.validate_score)
            ciencias = self._ask("Ingrese la nota de Ciencias (0-100): ", Student.validate_score)

            self.add(Student(nombre, seccion, espanol, ingles, sociales, ciencias))
            print(f"The student {nombre} has been added successfully.")

            if not self._ask_yes_no("\nDo you want to enter another student? (y/n): "):
                break

    def show_students(self):
        if not self._students:
            print("\n There are no students registered.")
            return

        print("\n==================== Students List ====================")
        for i, s in enumerate(self._students, 1):
            print(f"{i}. {s} -> "
                  f"Esp: {s.espanol} | Ing: {s.ingles} | Soc: {s.sociales} | Cie: {s.ciencias} | Prom: {s.average:.2f}")
        print("==============================================================")

    def show_top_3(self):
        if not self._students:
            print("\n There are no students to generate the Top 3.")
            return

        print("\n TOP 3 BEST AVERAGES ")
        for i, s in enumerate(self.top(3), 1):
            print(f" #{i} - {s.nombre} ({s.seccion}) - Average: {s.average:.2f}")

    def show_average(self):
        if not self._students:
            print("\n There are no students to calculate the general average.")
            return

        print(f"\n General score is: {self.general_average():.2f}")

    def show_failed_students(self):
        """Shows students who have at least one subject with a grade below 60 (Extra Requirement)."""
        if not self._students:
            print("\n There are no students registered.")
            return

        print("\n FAILED STUDENTS (Subjects with grade < 60) ")
        failed = self.failed_students()
        for s in failed:
            subjects = ", ".join(f"{name.capitalize()} ({score})" for name, score in s.failed_subjects().items())
            print(f"- {s} -> Failed: {subjects}")

        if not failed:
            print("No student has failed any subjects.")

    def delete_student(self):
        if not self._students:
            print("\n There are no students to delete.")
            return

        print("\n--- Remove Student ---")
        nombre = input("Type the student full name: ").strip()
        seccion = input("Enter the student's section: ").strip().upper()

        student = self.find(nombre, seccion)
        if not student:
            print(" Error: The student does not exist with that name and section.")
            return

        if self._ask_yes_no(f" Are you sure you want to delete {student.nombre} from section {student.seccion}? (y/n): "):
            self.remove(student)
            print(" Student deleted successfully.")
        else:
            print(" Operation cancelled.")

    def export_data(self):
        self._repository.save(self._students)

    def import_data(self):
        imported = self._repository.load()
        if imported:
            self._students = imported
