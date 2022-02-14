# tests using pytest
from src.jogo import play
from pytest import mark

""" The tests are formed for 3 steps (GWT method):
- Given = Data
- When
- Then
"""


@mark.return1
def test_when_play_should_return_1():
    # ----- long code version
    # it should return 1
    entry = 1  # data
    expected = 1  # data
    result = play(entry)  # when
    assert result == expected  # then


@mark.return2
def test_when_play_should_return_2():
    assert play(2) == 2


@mark.returnCheese
def test_when_play_return_cheese():
    assert play(3) == 'CHEESE'


@mark.returnSweetCheese
def test_when_play_return_sweet_cheese():
    assert play(5) == 'SWEET CHEESE'


# using the mark skip - it will skip the test when it's not implemented yet
@mark.skip(reason="not implemented yet")
def test_when_play_return_1_then_none():
    assert play(20) == 'SWEET CHEESE'


# this test will return 5 tests, cuz I'm passing 5 numbers on entry numbers to return on the test
@mark.parametrized
@mark.parametrize(
    'entry',
    [5, 10, 20, 25, 35]
)
def test_play_must_return_sweet_cheese_with_5_multiples():
    assert play(10) == 'SWEET CHEESE'
