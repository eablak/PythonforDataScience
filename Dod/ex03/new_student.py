import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = name[0].upper() + surname