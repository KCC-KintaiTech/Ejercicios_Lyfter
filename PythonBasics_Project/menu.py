"*** Python Basics - Final Project: Student Management"
"*** Module Name:  menu.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-07-11"
"*** Notes:  Displays the available options in the system."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"

def show_options():
    """ Displays the available menu options."""
    print("\n=== Lyfter Students Califications Records ===")
    print("1. Register a new student")
    print("2. Show all students")
    print("3. Show Top 3 students")
    print("4. Show overall average")
    print("5. Show failed students ")
    print("6. Delete a student ")
    print("7. Export data to CSV")
    print("8. Import data from CSV")
    print("9. Exit")
    print("====================================")

def execute_menu() -> str:
    """Shows options and validates the user's choice."""
    while True:
        show_options()
        opcion = input("Select an option (1-9): ").strip()
        if opcion in [str(i) for i in range(1, 10)]:
            return opcion
        print(" Invalid option. Please try again by entering a number from 1 to 9.")