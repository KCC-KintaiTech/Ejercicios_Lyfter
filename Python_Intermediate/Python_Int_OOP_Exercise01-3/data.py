"*** Python Basics - Final Project: Student Management"
"*** Module Name:  data"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-07-18"
"*** Notes:  Defines the repository class that saves and loads Student objects from a CSV file."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"
import csv
import os

from student import Student


class CsvStudentRepository:
    """Saves a list of Student objects to a CSV file and loads them back."""

    def __init__(self, filename: str = r"c:\Publico\LyfterStudents.csv"):
        self.filename = filename

    def save(self, students: list) -> bool:
        """Exports the students to the CSV file (each Student is converted to a dictionary)."""
        if not students:
            print("\n There are no student records to export, check it out.")
            return False

        try:
            with open(self.filename, mode="w", newline="", encoding="utf-8") as file_struct:
                writer = csv.DictWriter(file_struct, fieldnames=Student.FIELDNAMES)
                writer.writeheader()
                for student in students:
                    writer.writerow(student.to_dict())
            print(f"\n Students records exported successfully to '{self.filename}'.")
            return True
        except IOError as e:
            print(f"\n There was an error writing the file: {e}")
            return False

    def load(self) -> list:
        """Imports the CSV file and returns a list of Student objects."""
        if not os.path.exists(self.filename):
            print(f"\n The file '{self.filename}' does not exist. No previous data found.")
            return []

        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                students = [Student.from_dict(row) for row in csv.DictReader(file)]
            print(f"\n Total of {len(students)} students were imported successfully.")
            return students
        except (IOError, ValueError, KeyError) as e:
            print(f"\n There was an error reading or processing the CSV file: {e}")
            return []
