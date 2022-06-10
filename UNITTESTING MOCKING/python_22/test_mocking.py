from unittest import mock
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

