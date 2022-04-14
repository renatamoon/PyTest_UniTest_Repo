from tutorial1.myapp.sample import guess_number
from unittest import mock
import pytest


@pytest.mark.parametrize("_input,expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("tutorial1.myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3  # setting the return value of the roll dice function to 3. So it will always be 3
    assert guess_number(_input) == expected

    mock_roll_dice.assert_called_once()  # assert if the function were called only one time

# the "mock_roll_dice" inside the is equals to === mock_roll_dice = mock.Mock(name="roll dice mock", return_value=3)
# then it is only the mocked object you're trying to catch
# the parametrization you can pass the "input expected" and then you pass the expected values to it

if __name__ == '__main__':
    pytest.main()