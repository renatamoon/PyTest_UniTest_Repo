# tests using pytest
from src.jogo import play

""" The tests are formed for 3 steps (GWT method):
- Given = Data
- When
- Then
"""


def test_when_play_should_return_1():
    # ----- long code version
    # it should return 1
    entry = 1  # data
    expected = 1  # data
    result = play(entry)  # when
    assert result == expected  # then

    # ----- small code version
