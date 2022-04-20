from totorial_fixture.mydb import MyDB
import pytest

"""
Second method is using the fixtures.
"""

conn = None
cur = None


@pytest.fixture
def cursor_db():
    db = MyDB()
    conn = db.connect("server")  # this should be a connection string
    cur = conn.cursor()
    return cur


# so when you call the function cursor_db
# (that is a fixture) you will execute the fixture function and will return the expected value
def test_johns_id(cursor_db):
    query = "select id from employee_db where name=John"
    id_query = cursor_db.execute(query=query)
    assert id_query == 123


def test_toms_id(cursor_db):
    query = "select id from employee_db where name=Tom"
    id_query = cursor_db.execute(query=query)
    assert id_query == 789
