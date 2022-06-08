from unittest import mock, TestCase
from tutorial3.main import main


class TestExamples(TestCase):

    def test_print_contents_of_cwd_success(self):
        actual_result = main.print_contents_of_cwd()

        expected_directory = b'tests'
        self.assertIn(expected_directory, actual_result)

