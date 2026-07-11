"*** Python Basics - Final Project: Student Management"
"*** Module Name:  actions.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-07-04"
"*** Notes:  This module provides functions to validate student data and calculate averages."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"

import re

def calculate_average_score(student_dictionary: dict) -> float:
    """Calculate the average score of a student across four subjects."""
    student_scores = [student_dictionary["espanol"], student_dictionary["ingles"], student_dictionary["sociales"], student_dictionary["ciencias"]]
    return sum(student_scores) / len(student_scores)

def is_valid_name(student_name: str) -> bool:
    """Validates student name is not empty, contains letters and spaces, and no numbers."""
    clean_name = student_name.strip()
    if not clean_name:
        return False
    # important: allows letters (including accented), spaces, and no numbers or symbols in Spanish names
    return bool(re.match(r"^[A-Za-zÁéíóúÁÉÍÓÚñÑ\s]+$", clean_name))

def is_valid_section(Student_section: str) -> bool:
    """Validates the section format (e.g., 10A, 11B). A digit or two followed by a letter."""
    return bool(re.match(r"^\d{1,2}[A-Za-z]$", Student_section.strip()))

def student_exists(student_name: str, Student_section: str, students_list: list) -> bool:
    """Verifies if a student with the same name and section already exists (case-insensitive)."""
    for est in students_list:
        if est["nombre"].lower().strip() == student_name.lower().strip() and est["seccion"].lower().strip() == Student_section.lower().strip():
            return True
    return False

def request_score(subject_name: str) -> float:
    """Asks for and validates a grade between 0 and 100."""
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {subject_name} (0-100): "))
            if 0 <= nota <= 100:
                return nota
            print(" Score should be between 0 and 100.")
        except ValueError:
            print(" Invalid input. Please enter a number.")

def register_students(students_list: list):
    """Allows the entry of multiple students one at a time."""
    while True:
        print("\n--- New Student Record ---")
        
        # Validates Name
        while True:
            nombre = input("Full Name: ").strip()
            if is_valid_name(nombre):
                break
            print(" Invalid name. It should not be empty and should only contain letters and spaces.")

        # Validates Section
        while True:
            seccion = input("Section (e.g., 11B): ").strip().upper()
            if is_valid_section(seccion):
                break
            print(" Invalid section format. It should be like '10A' or '11B'.")
            
        # Validates Duplicates
        if student_exists(nombre, seccion, students_list):
            print(f" The student '{nombre}' is already registered in section '{seccion}'.")
            keep_adding = input("Do you want to try with another student? (y/n): ").lower()
            if keep_adding != 'y':
                break
            continue

        # Request Scores for Each Subject
        espanol = request_score("Español")
        ingles = request_score("Inglés")
        sociales = request_score("Sociales")
        ciencias = request_score("Ciencias")
        
        new_student = {
            "nombre": nombre,
            "seccion": seccion,
            "espanol": espanol,
            "ingles": ingles,
            "sociales": sociales,
            "ciencias": ciencias
        }
        
        students_list.append(new_student)
        print(f"The student {nombre} has been added successfully.")
        
        keep_adding = input("\nDo you want to enter another student? (y/n): ").lower()
        if keep_adding != 'y':
            break

def show_students(students_list: list):
    """Shows the list of all students."""
    if not students_list:
        print("\n There are no students registered.")
        return
        
    print("\n==================== Students List ====================")
    for i, stu_all in enumerate(students_list, 1):
        prom = calculate_average_score(stu_all)
        print(f"{i}. {stu_all['nombre']} [{stu_all['seccion']}] -> "
              f"Esp: {stu_all['espanol']} | Ing: {stu_all['ingles']} | Soc: {stu_all['sociales']} | Cie: {stu_all['ciencias']} | Prom: {prom:.2f}")
    print("==============================================================")

def show_top_3(students_list: list):
    """Shows the Top 3 of students with the best average."""
    if not students_list:
        print("\n There are no students to generate the Top 3.")
        return
        
    # Sort students by average score in descending order
    students_sorted = sorted(students_list, key=calculate_average_score, reverse=True)
    
    print("\n TOP 3 BEST AVERAGES ")
    for i, stu_all in enumerate(students_sorted[:3], 1):
        stu_avg = calculate_average_score(stu_all)
        print(f" #{i} - {stu_all['nombre']} ({stu_all['seccion']}) - Average: {stu_avg:.2f}")

def show_average(students_list: list):
    """Shows the average of all students' averages."""
    if not students_list:
        print("\n There are no students to calculate the general average.")
        return
        
    total_scores = sum(calculate_average_score(est) for est in students_list)
    general_score = total_scores / len(students_list)
    print(f"\n General score is: {general_score:.2f}")

def show_failed_students(students_list: list):
    """Shows students who have at least one subject with a grade below 60 (Extra Requirement)."""
    if not students_list:
        print("\n There are no students registered.")
        return
        
    failed_found = False
    print("\n FAILED STUDENTS (Subjects with grade < 60) ")
    
    for stu_row in students_list:
        failed_subjects = []
        for subject_row in ["espanol", "ingles", "sociales", "ciencias"]:
            if stu_row[subject_row] < 60:
                failed_subjects.append(f"{subject_row.capitalize()} ({stu_row[subject_row]})")
                
        if failed_subjects:
            failed_found = True
            print(f"- {stu_row['nombre']} [{stu_row['seccion']}] -> Failed: {', '.join(failed_subjects)}")
            
    if not failed_found:
        print("No student has failed any subjects.")

def delete_student(students_list: list):
    """delete student if confirmed by user."""
    if not students_list:
        print("\n There are no students to delete.")
        return
        
    print("\n--- Remove Student ---")
    nombre = input("Type the student full name: ").strip()
    seccion = input("Enter the student's section: ").strip().upper()
    
    student_found = None
    for stu_row in students_list:
        if stu_row["nombre"].lower() == nombre.lower() and stu_row["seccion"] == seccion:
            student_found = stu_row
            break
            
    if not student_found:
        print(" Error: The student does not exist with that name and section.")
        return
        
    confirmacion = input(f" Are you sure you want to delete {student_found['nombre']} from section {seccion}? (y/n): ").lower()
    if confirmacion == 'y':
        students_list.remove(student_found)
        print(" Student deleted successfully.")
    else:
        print(" Operation cancelled.")