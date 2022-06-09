# SETUP TEARDOWN DEMONSTRATION

def setup_module():
    print("OPEN DB CONNECTION")


def teardown_module():
    print("CLOSE DB CONNECTION")


def test_multiply():
    print("MULTIPLY EXECUTED")


def test_divide():
    print("DIVIDE EXECUTED")


def test_mod():
    print("MOD EXECUTED")
