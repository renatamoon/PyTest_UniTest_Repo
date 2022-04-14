import random
import time
import requests
from unittest import mock


def random_sum():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a + b


def silly():
    params = {
        "timestamp": time.time(),
        "number": random.randint(1, 6)
    }

    response = requests.get("https://httpbin.org/get", params)
    if response.status_code == 200:
        return response.json()['args']


# ---------- mocking the function

m = mock.Mock()
# m.return_value = 3  # setting the return_value as 3. So it should be always 3

m.side_effect = [1, 2, 3]

print(m())
