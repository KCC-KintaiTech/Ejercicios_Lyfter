"*** Python Basics - Final Project: Student Management"
"*** Module Name:  main.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-07-11"
"*** Notes:  This is the entry point of the student management system."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"

import menu
import actions
import data

def main():
    # Entry point of the system. Initializes an empty list for student records and handles user interactions.
    students_list = []
    
    while True:
        menu_option = menu.execute_menu()
        
        if menu_option == "1":
            actions.register_students(students_list)
        elif menu_option == "2":
            actions.show_students(students_list)
        elif menu_option == "3":
            actions.show_top_3(students_list)
        elif menu_option == "4":
            actions.show_average(students_list)
        elif menu_option == "5":
            actions.show_failed_students(students_list)
        elif menu_option == "6":
            actions.delete_student(students_list)
        elif menu_option == "7":
            data.export_data(students_list)
        elif menu_option == "8":
            # update the students_list with imported data if available
            data_uploaded = data.import_data()
            if data_uploaded:
                students_list = data_uploaded
        elif menu_option == "9":
            print("\n Logging out and exiting...")
            break

if __name__ == "__main__":
    main()