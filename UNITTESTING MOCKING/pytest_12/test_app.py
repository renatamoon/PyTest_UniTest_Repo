from .app import add


def test_add():
    if add(20, 20) == 40:
        print(" ---- WORKS")
    else:
        print(" ---- FAILED")


# SYNTAX OF ASSERTIONS: assert <condition>, <message>
def test_add_number():
    assert add(30, 40) == 70
    # assert add(20, 40) == 70, "Addition failed"  # you can add a message - ERROR:
    # pytest_12/test_app.py:15: AssertionError


# TYPES OF ASSERTIONS THAT CAN VALIDATE YOUR TESTS
def test_add_string():
    output = add("I love", " Python")
    print(output)

    assert type(output) is str
    assert "love" in output
    assert isinstance(output, str)
    assert 'I love Python' == output
