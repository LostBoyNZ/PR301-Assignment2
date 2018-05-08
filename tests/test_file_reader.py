from file_reader import FileReader
from unittest.mock import patch
import unittest
import sys
import io


class TestFileReader(unittest.TestCase):

    def test_fetch_text_file_with_correct_data(self):
        # Arrange
        file_name = "testdata\\test_data_2_rows.txt"
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996', 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        expected_result = {'A001': line1, 'Q001': line2}
        file = FileReader.fetch_text_file(file_name)

        # Act
        result = FileReader.fetch_text_contents(file, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_fetch_text_file_does_not_record_extra_field(self):
        # Arrange
        file_name = "testdata\\test_data_2_rows_extra_field.txt"
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996', 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        expected_result = {'A001': line1, 'Q001': line2}
        file = FileReader.fetch_text_file(file_name)

        # Act
        result = FileReader.fetch_text_contents(file, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_fetch_text_file_not_found_returns_nothing(self):
        # Arrange
        file_name = "testdata\\file_does_not_exist.txt"
        expected_result = None
        file = FileReader.fetch_text_file(file_name)

        # Act
        result = FileReader.fetch_text_contents(file, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_load_pickle_file(self):
        # Arrange
        test_file_name = "testdata\\test_pickle_load.txt"
        expected_data_from_file =\
            ['€\x03X\x1d\x00\x00\x00This is being saved to a fileq\x00.']
        result = ""

        # Act
        result = FileReader.load_pickle_file(FileReader, test_file_name)

        # Assert
        self.assertTrue(result == expected_data_from_file)

    def test_load_pickle_file_by_inputting_file_name(self):
        # Arrange
        user_input = "P"
        expected_data_from_file =\
            ['€\x03X\x1d\x00\x00\x00This is being saved to a fileq\x00.']
        result = ""

        # Act
        with patch('builtins.input', side_effect=user_input):
            result = FileReader.load_pickle_file(FileReader)

        # Assert
        self.assertTrue(result == expected_data_from_file)

    def test_load_pickle_file_error_by_inputting_wrong_file_name(self):
        # Arrange
        user_input = "A"
        expected_string = "File not found"
        result = ""

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            result = FileReader.load_pickle_file(FileReader)
        sys.stdout = sys.__stdout__

        # Assert
        self.assertTrue(expected_string in captured_output.getvalue())
