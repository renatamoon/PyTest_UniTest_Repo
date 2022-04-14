from unittest import mock

from tutorial2.myapp.sample import random_sum


@mock.patch("tutorial2.myapp.sample.random.randint")  # here's the path of the function you want to mock
def test_random_sum(mock_randint):  # here's the mock object of the function
    mock_randint.side_effect = [3, 4]  # these are the values you want to set for the function to receive it
    assert random_sum() == 7
