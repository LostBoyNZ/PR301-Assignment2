import io
import sys
from file_controller import FileController
from unittest.mock import patch
import unittest
import random
import string


class TestFileReader(unittest.TestCase):

    def test_call_file_reads_text_file(self):
        # Arrange
        random_file_name = ''.join(random.sample(string.ascii_lowercase, 8))
        random_file_name = "temp\\" + random_file_name + ".txt"
        user_input = ['testdata\\test_data.txt', 'Y', 'F', random_file_name]
        expected_string = "File saved, 28 rows added"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileController.call_file(FileController, "", ",")
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_string in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)

    def test_call_file_reads_excel_file(self):
        # Arrange
        random_file_name = ''.join(
            random.sample(string.ascii_lowercase, 8))
        random_file_name = "temp\\" + random_file_name + ".txt"
        user_input = ['testdata\\test_data.xlsx', 'Y', 'F', random_file_name]
        expected_string = "File saved, 28 rows added"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileController.call_file(FileController, "", ",")
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_string in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)

    def test_call_file_returns_file_not_found_error_with_no_text_file(self):
        # Arrange
        random_file_name = ''.join(
            random.sample(string.ascii_lowercase, 8))
        random_file_name = "temp\\" + random_file_name + ".txt"
        user_input = ['no_file_here.txt', 'Y', 'F', random_file_name]
        expected_string = "File not found"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileController.call_file(FileController, "", ",")
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_string in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)

    def test_call_file_returns_file_not_found_error_with_no_excel_file(self):
        # Arrange
        random_file_name = ''.join(
            random.sample(string.ascii_lowercase, 8))
        random_file_name = "temp\\" + random_file_name + ".txt"
        user_input = ['no_file_here.xlsx', 'Y', 'F', random_file_name]
        expected_string = "File not found"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileController.call_file(FileController, "", ",")
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_string in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)

    def test_check_path_exists_returns_true_if_it_does_exist(self):
        # Arrange
        file_name = "testdata\\test_data.txt"
        expected_result = True

        # Act
        result = FileController.check_path_exists(file_name)

        # Assert
        self.assertTrue(result == expected_result)

    def test_check_path_exists_returns_false_if_it_does_not_exist(self):
        # Arrange
        file_name = "no_file_here.txt"
        expected_result = False

        # Act
        result = FileController.check_path_exists(file_name)

        # Assert
        self.assertTrue(result == expected_result)
