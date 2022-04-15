# PYTEST & UNITTEST - MOCKING FUNCTIONS WITH PATCH OBJECT

<hr>

### HOW TO USE THE MOCKING FUNCTION WITH PYTEST:

- ```mock.patch('package.module.ClassName')``` - it takes one positional argument - package - module that it's holding the class or function, then the Class name. It's important to know that you need to mock not where the object is defined but where it is used and those maybe are not
in the same place.

- ```mock.patch('package.module.ClassName', return_value='any')``` - This will enable to specify the return value of the function that has the patch applied. This is one of the main ways
to put an expected behavior to the patched function

- ```mock.patch('package.module.ClassName', side_effect=Exception('boom!'))``` </b>- it's another key argument to enable to put side effects where the function is being patched
<hr>

### Ways to apply the mock:</b>
* decorator: @
* context manager
* inline

<hr>

### DOCUMENTATION OF PYTEST AND MOCK FUNCTIONALITIES

https://docs.python.org/3/library/unittest.mock.html