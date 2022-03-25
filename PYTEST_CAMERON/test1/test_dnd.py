from dnd import attack_damage
from unittest import mock


# first you need to pass the function that you wanna mock
# the expected value (return value) of this function must always be 5
# include the "mock_randint" argument on the function to get the mock
# autospec argumento must be passed cause it will take all the arguments of the function

@mock.patch("dnd.randint", return_value=5, autospec=True)
def test_attack_damage(mock_randint):
    assert attack_damage(1) == 6
    