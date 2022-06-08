# PyTest_UniTest_Repo

### ADVANTAGES OF UNIT TESTING

- Find bugs early
- Reduce cost
- Improved quality of code
- improve debugging

### WHAT IS PYTEST?

- Pytest is a Python based testing framework for python, which is used to write or execute test cases for your software. POpular among the community.

### Advantage of Pytest

- Free and open source
- Easy to learn and use because of its simplicity
- Can run tests in parallel
- Offer various features like you can skip tests, you can set order for execution of tests, etc.

### HOW TO INSTALL BY THE COMMAND LINE?

- `pip install pytest`

### WHAT ARE ASSERTIONS?

- Assertions help programmers verify the output of a particular function or part of software;
- We write assertions to test our assumptions around a particular piece of coude.
- When the assertion is executed it is assumed to be true, if the assumption is not correct then the tests fails;
- we cannot validate the output with an if else statement

### SYNTAX OF ASSERTIONS

- assert <condition>, <message>

### TYPES OF ASSERTIONS

```def test_add_string():
    output = add("I love", " Python")
    print(output)

    assert type(output) is str
    assert "love" in output
    assert isinstance(output, str)
    assert 'I love Python' == output```
    
    
