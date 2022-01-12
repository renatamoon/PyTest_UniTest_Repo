
# PYTEST with the https://www.youtube.com/watch?v=snDSB9b8v_E


def test_1():
    x = 10
    y = 20
    assert x == y


def test_2():
    name = "selenium"
    title = "Selenium is for web automation"
    assert name in title


def test_3():
    name = "jenkins"
    title = "Jenkins is CI server"
    assert name in title, "Title does not match"