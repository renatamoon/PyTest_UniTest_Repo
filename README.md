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

```
def test_add_string():
    output = add("I love", " Python")
    print(output)

    assert type(output) is str
    assert "love" in output
    assert isinstance(output, str)
    assert 'I love Python' == output
```

### DEALING WITH EXEPTIONS

```
def test_exception_example():
    with pytest.raises(ZeroDivisionError, match=r".* by1 .*") as exceptinfo:
        print(100 / 0)
    print(type(exceptinfo))
    print(exceptinfo.type)
    print(exceptinfo.value)
    print(exceptinfo.traceback)
```

### USING MARKERS - XFAIL, XPASS AND XSKIP
    
- There will be scenarios that you wanna to scape of an error and also say that your peace of code must not pass.
- xfail - if the test is marked as xfail - then the test is executed but not considered in final result of execution.
- @pytest.mark.xfail
- Is helpful if you are expecting a test case to fail already
- REASON: You can also input a reason to be printed, this test will be executed but it will be passed:
    
```
@pytest.mark.xfail(reason="SHOULD BE SKIPPED")
def test_add():
    assert add(10, 20) == 30
```

- Another example is to use sys.version_info as a parameter and then use a reason that your test can fail:
    
```
@pytest.mark.xfail(sys.version_info > (3, 7), reason="Python module version not compatible")
def test_divide():
    assert divide(20, 10) == 2   
```

### PARAMETRIZE

- Parametrize allows us to pass the values that we want to use as parameters and also set an OUTPUT for it we can use it for a lot of parameters as we can see on the example. Also, different types of parameters;
    
```
@pytest.mark.parametrize("output, a, b", [
                             (30, 10, 20),
                             (300, 100, 200),
                             (3000, 1000, 2000)],
                         ids=["first", "second", "third"])
def test_add_parametrize(output, a, b):
    assert add(a, b) == output
    
```

### USING MOCK ON UNIT TESTS:
    
- Should not depend on any type of lib, database, server or service. What is a dependence? IS something your
code is using as a dependency.
- When you're testing your service, you need to get rid of all the dependencies. Then, when you need to use the
dependencies you should call the Mock of your database, email service or location API.
    

#### BENEFITS OF MOCKING:
    
- Cut down the external dependencies;
- run test in isolation;
- Save time while executing tests
- Gives you more control on simulating the behavior of external dependencies/libraries
