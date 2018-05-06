from file_reader import FileReader
import unittest


class TestFileReader(unittest.TestCase):

    def test_split_file_with_correct_data(self):
        # Arrange
        file_name = "testdata\\test_data_2_rows.txt"
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996', 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        expected_result = {'A001': line1, 'Q001': line2}

        # Act
        result = FileReader.split_file(FileReader, file_name, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_split_file_does_not_record_extra_field(self):
        # Arrange
        file_name = "testdata\\test_data_2_rows_extra_field.txt"
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996', 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        expected_result = {'A001': line1, 'Q001': line2}

        # Act
        result = FileReader.split_file(FileReader, file_name, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_split_file_not_found_returns_nothing(self):
        # Arrange
        test_name = "file_reader Class, split_file Method, Test #3"
        file_name = "testdata\\file_does_not_exist.txt"
        expected_result = None

        # Act
        result = FileReader.split_file(FileReader, file_name, "", ",")

        # Assert
        self.assertTrue(result == expected_result)
