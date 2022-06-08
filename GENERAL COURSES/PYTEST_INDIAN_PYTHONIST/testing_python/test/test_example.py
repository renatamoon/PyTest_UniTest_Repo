import unittest
import pytest

from testing_python.main.example import replace_indiana

example_text = """
        Henry Jones, Jr., ou simplesmente Indiana Jones, é um personagem da série de filmes Indiana Jones, 
        criado por George Lucas e Steven Spielberg, George lucas criou o personagem em homenagem aos heróis de 
        séries e filmes de ação dos anos 1930. O personagem apareceu pela primeira vez em 1981 em Indiana Jones e 
        Os Caçadores da Arca Perdida, dirigido por Steven Spielberg e vivido por Harrison Ford. 
        O personagem também aparece em séries de televisão.
"""


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.text = example_text

    def test_given_a_text_with_indiana_replacement_return_text_without_indiana_and_using_proper_name_instead(self):
        # Given param
        proper_name = "Dr."

        # When
        result_text, result_count = replace_indiana(self.text, proper_name)

        # Then
        self.assertEqual(result_count, 3)
        self.assertIsNot(result_text, self.text)
        self.assertNotIn("indiana", result_text)
        self.assertIn(proper_name, result_text)

    def test_dummy_fail_test(self):
        proper_name = "Dr."

        result_text, result_count = replace_indiana(self.text, proper_name)

        self.assertEqual(result_count, 3)


def test_given_a_text_with_indiana_replacement_return_text_without_indiana():
    # Given parameters
    text = example_text
    proper_name = "Dr."

    # what happens WHEN
    result_text, result_count = replace_indiana(text, proper_name)

    # What happens THEN
    assert result_count == 3
    assert result_text is not text
    assert "indiana" not in result_text
    assert proper_name in result_text


