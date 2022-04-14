from unittest import mock

# ---------- mocking the function

m = mock.Mock()
m.return_value = 3  # setting the return_value as 3. So it should be always 3

# m.return_value = 3
m.side_effect = [1, 2, 3, ZeroDivisionError()]
"""Side effect is the property you need to set to provide the output of the mocked function.
So if you put a value to a side effect, then you will receive the value of it each time you call the mocking function
You can also put EXCEPTIONS inside of the side effect. It also helps you to define exceptions"""

print(m())  # 1
print(m())  # 2
print(m())  # 3
print(m())  # ZeroDivisionError

m.return_value = ZeroDivisionError()
print(m())
