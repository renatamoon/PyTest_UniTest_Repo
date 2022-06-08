from run import function_to_return_the_name
from generator import set_keyboard_input, get_display_output


def test_1():
    set_keyboard_input(["Renata", "Spock"])

    # that's the function that will be tested
    function_to_return_the_name()

    output = get_display_output()

    assert output == ["Hi", "Tell me your name: ", "Tell me your pet's name: "]