"*** Python Basics - Final Project: Student Management"
"*** Module Name:  data"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-06-28"
"*** Notes:  This module provides functions to export student records to a CSV file and import them back into the program."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"
import csv
import os

student_FILENAME = r"c:\Publico\LyfterStudents.csv"

def export_data(students: list) -> bool:
    """Download student list to a CSV file in C:\Publico."""
    if not students:
        print("\n There are no student records to export, check it out.")
        return False
        
    try:
        with open(student_FILENAME, mode="w", newline="", encoding="utf-8") as file_struct:
            # Define the fieldnames for the CSV file based on the student dictionary keys
            fieldnames = ["nombre", "seccion", "espanol", "ingles", "sociales", "ciencias"]
            writer = csv.DictWriter(file_struct, fieldnames=fieldnames)
            
            writer.writeheader()
            for est in students:
                writer.writerow(est)
        print(f"\n Students records exported successfully to '{student_FILENAME}'.")
        return True
    except IOError as e:
        print(f"\n There was an error writing the file: {e}")
        return False

def import_data() -> list:
    """Import student records from the CSV file if it exists."""
    if not os.path.exists(student_FILENAME):
        print(f"\n The file '{student_FILENAME}' does not exist. No previous data found.")
        return []
        
    students = []
    try:
        with open(student_FILENAME, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "nombre": row["nombre"],
                    "seccion": row["seccion"],
                    "espanol": float(row["espanol"]),
                    "ingles": float(row["ingles"]),
                    "sociales": float(row["sociales"]),
                    "ciencias": float(row["ciencias"])
                }
                students.append(student)
        print(f"\n Total of {len(students)} students were imported successfully.")
        return students
    except (IOError, ValueError, KeyError) as e:
        print(f"\n There was an error reading or processing the CSV file: {e}")
        return []