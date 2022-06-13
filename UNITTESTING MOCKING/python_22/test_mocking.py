from unittest import mock
from service import is_available

"""
USING MOCK:
- Should not depend on any type of lib, database, server or service. What is a dependence? IS something your
code is using as a dependency.
- When you're testing your service, you need to get rid of all the dependencies. Then, when you need to use the
dependencies you should call the Mock of your database, email service or location API.

BENEFITS OF MOCKING:
- Cut down the external dependencies;
- run test in isolation;
- Save time while executing tests
- Gives you more control on simulating the behavior of external dependencies/libraries
"""

first_mock = mock.Mock()
second_mock = mock.Mock(name="My first Mock")
first_mock()

first_mock_value = mock.Mock(name="First Mock", return_value=False)
first_mock_value()


@mock.patch("python_22.service.check_availability")
def test_first_mock(mock_check_availability):
    first_mock.return_value = False
    print(is_available())
    first_mock.assert_called()  # when the mock was called at least one time
    first_mock.assert_called_once()  # when the mock was called exactly once


"""
There are other VERIFYING MOCKS
- assert called - when the mock was called at least one time
- assert called with - when the mock was called exactly once
- assert not called - when the mock wasn't called at all
- assert called with - when the mock was called with arguments or parameters
- assert called once with - when the mock was called exactly once with arguments/parameters
"""
