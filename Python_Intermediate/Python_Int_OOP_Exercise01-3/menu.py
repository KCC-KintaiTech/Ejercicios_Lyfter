"*** Python Intermediate - Refactory of Project: Student Management using OOP"
"*** Module Name:  menu.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2026-11-15"
"*** Notes:  Defines the Menu class that displays the available options and validates the user's choice."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"


class Menu:
    """Console menu. Options are given as an ordered list of (label, action) pairs."""

    def __init__(self, title: str, options: list):
        self.title = title
        self.options = options

    def show_options(self):
        print(f"\n=== {self.title} ===")
        for number, (label, _) in enumerate(self.options, 1):
            print(f"{number}. {label}")
        print("====================================")

    def choose(self):
        """Shows the options until the user picks a valid one and returns its action."""
        while True:
            self.show_options()
            choice = input(f"Select an option (1-{len(self.options)}): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(self.options):
                return self.options[int(choice) - 1][1]
            print(f" Invalid option. Please try again by entering a number from 1 to {len(self.options)}.")
