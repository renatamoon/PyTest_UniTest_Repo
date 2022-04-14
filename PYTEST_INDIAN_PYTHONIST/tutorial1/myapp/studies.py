from unittest import mock
import random

import requests


def roll_dice():
    print("rolling ...")
    return random.randint(1, 6)


print(roll_dice())

# ---------
mock_roll_dice = mock.Mock(name="roll dice mock", return_value=3)
print(mock_roll_dice())  # <Mock name='mock()' id='3083720879664'>

mock_roll_dice_1 = mock.Mock(name="roll dice mock")
print(mock_roll_dice_1)

# --------- assertion to check how many times the function was called
mock_roll_dice.assert_called()

# ---------------------------------------


def get_ip():
    response = requests.get("https://meuip.com.br/")
    if response.status_code == 200:
        return response.json()


# get_ip()
#
# mock_response = mock.Mock(return_value=2, status_code=200, "json.return_value": {"origin": "0.0.0.0"})
# mock_response.json.return_value = {"origin": "0.0.0.0"}
# mock_response.status_code
#
# mock_response.json()
