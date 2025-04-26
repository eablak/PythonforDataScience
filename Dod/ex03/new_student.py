import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-letter lowercase ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class representing a student with automatically generated login and ID.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Student's active status, default is True.
        login (str): Auto-generated login based on name and surname.
        generate_id (str): Auto-generated random ID for the student.
    """
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    generate_id: str = field(init=False)

    def __post_init__(self):
        """Generate login and ID after initializing the student."""
        self.login = self.name[0].upper() + self.surname
        self.generate_id = generate_id()
