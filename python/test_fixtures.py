import pytest

@pytest.fixture
def user():
    return {"name": "vlad", "age": 27}      # верни словарь {"name": "Влад", "age": 27}

def test_user_name(user):
    assert user["name"] == "vlad"

def test_user_age(user):
    assert user["age"] == 27


@pytest.fixture
def connection():
    print("\nподключаюсь к БД")        # setup
    conn = {"connected": True}
    yield conn                           # отдай conn тесту
    print("\nзакрываю подключение")     # teardown

def test_connection(connection):
    assert connection["connected"] is True



@pytest.fixture(scope="module")   # scope по умолчанию: function
def counter():
    print("\nсоздаю counter")
    return {"value": 0}

def test_one(counter):
    counter["value"] += 1
    assert counter["value"] == 1

def test_two(counter):
    counter["value"] += 1
    assert counter["value"] == 1


@pytest.fixture
def person():
    return {"name": "Влад"}

@pytest.fixture
def greeting(person):          # одна фикстура просит другую
    return f"Привет, {person['name']}"

def test_greeting(greeting):
    assert greeting == "Привет, Влад"