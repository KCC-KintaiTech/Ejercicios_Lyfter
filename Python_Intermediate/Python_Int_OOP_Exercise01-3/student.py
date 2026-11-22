"*** Python Basics - Final Project: Student Management"
"*** Module Name:  student.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2024-07-18"
"*** Notes:  Defines the Student class. A Student validates and protects its own data."
"            Code and documentation are provided in English but file structure is in Spanish to comply with requirements."
"*************************************************************************************************"

import re


class Student:
    """A student with a name, a section and four subject scores.

    Every attribute is validated in its setter, so a Student can never hold invalid data.
    """

    SUBJECTS = ["espanol", "ingles", "sociales", "ciencias"]
    FIELDNAMES = ["nombre", "seccion"] + SUBJECTS
    MIN_SCORE = 0
    MAX_SCORE = 100
    PASSING_SCORE = 60

    def __init__(self, nombre: str, seccion: str, espanol: float, ingles: float,
                 sociales: float, ciencias: float):
        self.nombre = nombre
        self.seccion = seccion
        self.espanol = espanol
        self.ingles = ingles
        self.sociales = sociales
        self.ciencias = ciencias

    # ---------- Validation (reusable without creating a Student) ----------

    @staticmethod
    def validate_name(name: str) -> str:
        """Returns the cleaned name or raises ValueError (letters and spaces only, not empty)."""
        clean_name = str(name).strip()
        if not clean_name:
            raise ValueError("Invalid name. It should not be empty.")
        if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", clean_name):
            raise ValueError("Invalid name. It should only contain letters and spaces.")
        return clean_name

    @staticmethod
    def validate_section(section: str) -> str:
        """Returns the section in upper case (e.g., 11B) or raises ValueError."""
        clean_section = str(section).strip().upper()
        if not re.match(r"^\d{1,2}[A-Z]$", clean_section):
            raise ValueError("Invalid section format. It should be like '10A' or '11B'.")
        return clean_section

    @staticmethod
    def validate_score(score) -> float:
        """Returns the score as a float or raises ValueError if it is not a number between 0 and 100."""
        try:
            number = float(score)
        except (TypeError, ValueError):
            raise ValueError("Invalid input. Please enter a number.")
        if not Student.MIN_SCORE <= number <= Student.MAX_SCORE:
            raise ValueError(f"Score should be between {Student.MIN_SCORE} and {Student.MAX_SCORE}.")
        return number

    # ---------- Attributes (properties validate on every assignment) ----------

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = self.validate_name(value)

    @property
    def seccion(self) -> str:
        return self._seccion

    @seccion.setter
    def seccion(self, value: str):
        self._seccion = self.validate_section(value)

    @property
    def espanol(self) -> float:
        return self._espanol

    @espanol.setter
    def espanol(self, value):
        self._espanol = self.validate_score(value)

    @property
    def ingles(self) -> float:
        return self._ingles

    @ingles.setter
    def ingles(self, value):
        self._ingles = self.validate_score(value)

    @property
    def sociales(self) -> float:
        return self._sociales

    @sociales.setter
    def sociales(self, value):
        self._sociales = self.validate_score(value)

    @property
    def ciencias(self) -> float:
        return self._ciencias

    @ciencias.setter
    def ciencias(self, value):
        self._ciencias = self.validate_score(value)

    # ---------- Behavior ----------

    @property
    def average(self) -> float:
        """Average score across the four subjects."""
        scores = [getattr(self, subject) for subject in self.SUBJECTS]
        return sum(scores) / len(scores)

    def failed_subjects(self) -> dict:
        """Returns {subject: score} for every subject below the passing score."""
        return {subject: getattr(self, subject)
                for subject in self.SUBJECTS
                if getattr(self, subject) < self.PASSING_SCORE}

    def has_failed(self) -> bool:
        """True if the student failed at least one subject."""
        return bool(self.failed_subjects())

    # ---------- Conversion (CSV support) ----------

    def to_dict(self) -> dict:
        """Converts this student into a dictionary (used to export to CSV)."""
        return {field: getattr(self, field) for field in self.FIELDNAMES}

    @classmethod
    def from_dict(cls, row: dict) -> "Student":
        """Creates a Student from a dictionary (used when importing from CSV)."""
        return cls(**{field: row[field] for field in cls.FIELDNAMES})

    # ---------- Special methods ----------

    def __eq__(self, other) -> bool:
        """Two students are the same when name and section match (case-insensitive)."""
        if not isinstance(other, Student):
            return NotImplemented
        return (self.nombre.lower(), self.seccion) == (other.nombre.lower(), other.seccion)

    def __hash__(self) -> int:
        return hash((self.nombre.lower(), self.seccion))

    def __str__(self) -> str:
        return f"{self.nombre} [{self.seccion}]"

    def __repr__(self) -> str:
        return (f"Student({self.nombre!r}, {self.seccion!r}, {self.espanol}, "
                f"{self.ingles}, {self.sociales}, {self.ciencias})")
