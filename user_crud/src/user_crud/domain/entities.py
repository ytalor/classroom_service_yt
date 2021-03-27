from enum import Enum, unique
from typing import Optional, Union

from datetime import date
from dataclasses import dataclass

@unique
class Priority(Enum):
    LOWEST = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    HIGHTEST = 5


@dataclass
class User:
    """"Class definig a systems user"""
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: Union[date, str]
    age: int


    def __post_init__(self):
        if isinstance(self.birthday, str):
            self.birthday = date.fromisoformat(self.birthday)


    def __repr__(self):
        return (
            f"User {self.first_name} {self.last_name}, "
            f"born in {self.birthday.isoformat()}, "
            f"with e-mail {self.email} "
            f"at the age of {self.age}."
        )
