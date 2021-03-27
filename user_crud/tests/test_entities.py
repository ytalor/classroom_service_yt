import pytest
from datetime import date

from src.user_crud.domain.entities import User


@pytest.fixture(scope='session')
def user():
    return User(
        "Fulano", "de Tal",
        "fulano@detal.com", '123456789',
        "1992-04-16", 28
    )

def test_user_repr(user):
    
    expected_text = "User Fulano de Tal, born in 1992-04-16, with e-mail fulano@detal.com at the age of 28."
    #expected_text = "User Fulano de Tal, with e-mail fulano@detal.com at the age of 28."
    current_text = str(user)

    assert expected_text == current_text


def test_user_birthday(user):
    date_iso = user.birthday.isoformat()
    year, month, day = tuple(date_iso.split("-"))

    assert len(year) == 4
    assert len(month) == 2
    assert int(month) <= 12
    assert int(month) > 0
    assert len(day) == 2
    assert int(day) <= 31
    assert int(day) > 0

def test_date_instance(user):
    assert isinstance(user.birthday, date)