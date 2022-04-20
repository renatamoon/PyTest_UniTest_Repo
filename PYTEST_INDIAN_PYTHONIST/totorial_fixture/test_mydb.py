from totorial_fixture.mydb import MyDB


def test_johns_id():
    db = MyDB()
    conn = db.connect("server")  # this should be a connection string
    cur = conn.cursor()
    query = "select id from employee_db where name=John"
    id_query = cur.execute(query=query)
    assert id_query == 123


def test_toms_id():
    db = MyDB()
    conn = db.connect("server")  # this should be a connection string
    cur = conn.cursor()
    query = "select id from employee_db where name=Tom"
    id_query = cur.execute(query=query)
    assert id_query == 789


"""
The issue on these test are cuz they have: code repetition, creating expensive DB connection in every test case
Two ways to fix those issues:
1) setup and teardown methods (classic xunit style)
2) fixtures (recommended)
"""
