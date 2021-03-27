import pytest
import asyncio
from dotenv import load_dotenv

from src.user_crud.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student
)


loop = asyncio.get_event_loop()

@pytest.fixture()
def example_student():
    return {
        "fullname": "Test User",
        "email": "test@user.br",
        "course_of_study": "Computer engineering",
        "year": 5,
        "gpa": "3.0"
    }


@pytest.fixture()
def example_student_list():
    return [
        {
            "fullname": "Test User1",
            "email": "test@user.br",
            "course_of_study": "Computer engineering",
            "year": 5,
            "gpa": "3.0"
        },
        {
            "fullname": "Test User1",
            "email": "test@user.br",
            "course_of_study": "Computer engineering",
            "year": 5,
            "gpa": "3.0"
        },
        {
            "fullname": "Test User1",
            "email": "test@user.br",
            "course_of_study": "Computer engineering",
            "year": 5,
            "gpa": "3.0"
        },
        {
            "fullname": "Test User1",
            "email": "test@user.br",
            "course_of_study": "Computer engineering",
            "year": 5,
            "gpa": "3.0"
        }
    ]
        


def test_add_student(example_student):
    new_student = loop.run_until_complete(add_student(example_student))
    assert "id" in new_student.keys()


def test_retrieve_students(example_student_list):

    for student in example_student_list:
        _ = loop.run_until_complete(add_student(student))
    
    students = loop.run_until_complete(retrieve_students())

    assert len(students) > 1


def test_retrieve_student_data(example_student):
    new_student = loop.run_until_complete(add_student(example_student))
    retrieved_student = loop.run_until_complete(retrieve_student(new_student["id"]))

    assert new_student["id"] == retrieved_student["id"]

    loop.close()

