from totorial_fixture.mydb import MyDB

"""
First method is to setup and teardown methods (classic xunit style).
"""

conn = None
cur = None


def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect("server")  # this should be a connection string
    cur = conn.cursor()


def teardown_module(module):  # teardown means that you want to close the connections to the database
    cur.close()
    conn.close()


def test_johns_id():
    query = "select id from employee_db where name=John"
    id_query = cur.execute(query=query)
    assert id_query == 123


def test_toms_id():
    query = "select id from employee_db where name=Tom"
    id_query = cur.execute(query=query)
    assert id_query == 789
