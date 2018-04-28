import io
import sys
from pickle import dumps
import pickle
from file_reader import FileReader
from unittest.mock import patch
import unittest
import string
import random


class TestFileReader(unittest.TestCase):

    def test_split_file_with_correct_data(self):
        # Arrange
        filename = "testdata\\test_data_2_rows.txt"
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        expected_result = {'A001': line1, 'Q001': line2}

        # Act
        result = FileReader.split_file(FileReader, filename, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_split_file_does_not_record_extra_field(self):
        # Arrange
        filename = "testdata\\test_data_2_rows_extra_field.txt"
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        expected_result = {'A001': line1, 'Q001': line2}

        # Act
        result = FileReader.split_file(FileReader, filename, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_split_file_not_found_returns_nothing(self):
        # Arrange
        test_name = "file_reader Class, split_file Method, Test #3"
        filename = "testdata\\file_does_not_exist.txt"
        expected_result = None

        # Act
        result = FileReader.split_file(FileReader, filename, "", ",")

        # Assert
        self.assertTrue(result == expected_result)

    def test_write_to_database_with_valid_data(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        data_to_test = {'A001': line1, 'Q001': line2}
        expected_string_1 = "['A001', 'F,', '21,', '001,', 'Normal,', '12,', '01/01/1996,', '1']"
        expected_string_2 = "['Q001', 'M,', '45,', '999,', 'Underweight,', '725,', '31/12/1971,', '1']"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileReader.write_to_database(FileReader, data_to_test)  # Call the function I'm tests
        sys.stdout = sys.__stdout__

        # Check if the printed output includes the expected strings I'm looking for
        if expected_string_1 in captured_output.getvalue() and expected_string_2 in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)

    def test_save_pickle_file(self):
        # Arrange
        filename = "testdata\\test_pickle_save.txt"
        data_to_save = "This is being saved to a file"
        expected_data_loaded = "This is being saved to a file"

        # Act
        pickled = dumps(data_to_save)
        FileReader.commit_pickle_save(filename, pickled)    # Pickle

        # Open the file it just saved
        with open(filename, 'rb') as pickleFile:
            result = pickle.load(pickleFile)
        pickleFile.close()

        # Assert
        self.assertTrue(data_to_save == result)

    @patch('file_reader.FileReader.get_input', return_value='Y')
    def test_save_pickle_file_yes_saves_file(self, input):
        # Arrange
        data_to_save = "Something to pickle"
        pickled = dumps(data_to_save)

        # Act
        FileReader.save_pickle_file(FileReader, pickled)

        # Open the file it just saved, called Y because I can only submit
        # the same input to every request for input
        with open("Y", 'rb') as pickleFile:
            result = pickle.load(pickleFile)
        pickleFile.close()

        # Assert
        self.assertTrue(data_to_save == result)

    @patch('file_reader.FileReader.get_input', return_value='N')
    def test_save_pickle_file_no_does_not_save_file(self, input):
        # Arrange
        data_to_save = "Something to pickle"
        pickled = dumps(data_to_save)

        # Act
        FileReader.save_pickle_file(FileReader, pickled)

        # If a file called N exists, choosing no to saving the file failed
        try:
            open("N", 'rb')
        except FileNotFoundError:
            file_created = False
        else:
            file_created = True

        # Assert
        self.assertFalse(file_created)

    def test_commit_pickle_save(self):
        # Arrange
        filename = "testdata\\test_pickle_save.txt"
        data_to_save = "This is being saved to a file"
        expected_data_loaded = "This is being saved to a file"
        pickled = dumps(data_to_save)

        # Act
        FileReader.commit_pickle_save(filename, pickled)

        # Open the file it just saved
        with open(filename, 'rb') as pickleFile:
            result = pickle.load(pickleFile)
        pickleFile.close()

        # Assert
        self.assertTrue(data_to_save == result)

    def test_commit_save(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        file_target = "testdata\\test_file_to_write_to.txt"
        ids_already_in_file = []
        expected_output = "File saved, 2 rows added"

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileReader.commit_save(FileReader(), dict_valid, file_target, ids_already_in_file)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes the expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_commit_save_with_one_duplicate_key(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        file_target = "testdata\\test_file_to_write_to.txt"
        ids_already_in_file = ['A001']
        expected_output = "1 of 2 rows were duplicate keys and not inserted again"

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileReader.commit_save(FileReader(), dict_valid, file_target, ids_already_in_file)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes the expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_commit_save_with_all_duplicate_keys(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        file_target = "testdata\\test_file_to_write_to.txt"
        ids_already_in_file = ['A001', 'Q001']
        expected_output = "All ID's already existed in the output file. Nothing added."

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileReader.commit_save(FileReader(), dict_valid, file_target, ids_already_in_file)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes the expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    @patch('file_reader.FileReader.get_input', return_value='Y')
    def test_write_file(self, input):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        open("Y", 'w').close()      # Wipe the file for a fresh start

        # Act
        FileReader.write_file(FileReader, dict_valid)

        # Open the file it just saved
        with open("Y", 'rb') as file:
            result = file
        file.close()

        # Assert
        self.assertTrue(file)

    @patch('file_reader.FileReader.get_input', return_value='N')
    def test_write_file_do_not_write(self, input):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}

        # Act
        FileReader.write_file(FileReader, dict_valid)

        # If a file called N exists, choosing no to saving the file failed
        try:
            open("N", 'rb')
        except FileNotFoundError:
            file_created = False
        else:
            file_created = True

        # Assert
        self.assertFalse(file_created)

    def test_write_file_do_not_append_to_existing_file(self):
        # Arrange
        user_input = ['Y', 'F', "testdata\\file_already_exists.txt", "N", "Y", "F", "testdata\\new.txt", "Y"]
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_result = ['This file already exists']

        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader, dict_valid)

        # Assert
        file = open('testdata\\file_already_exists.txt')
        result = []
        for line in file:
            result.append(line)
        file.close()

        self.assertTrue(result == expected_result)

    def test_write_file_new_file(self):
        # Arrange
        random_filename = ''.join(random.sample(string.ascii_lowercase, 8))
        random_filename = "temp\\" + random_filename + ".txt"
        user_input = ['Y', 'F', random_filename]
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_result = ['\n', 'A001,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,\n']

        # Act
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader, dict_valid)

        # Assert
        file = open(random_filename)
        result = []
        for line in file:
            result.append(line)
        file.close()

        self.assertTrue(result == expected_result)

    def test_write_file_invalid_input(self):
        # Arrange
        user_input = ['Z']
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_output = "Invalid Input, please try again"

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader, dict_valid)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes the expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_write_file_choosing_database_option(self):
        # Arrange
        user_input = ['Y', "D"]
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_string_1 = "['A001', 'F,', '21,', '001,', 'Normal,', '12,', '01/01/1996,', '1']"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileReader.write_file(FileReader, dict_valid)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes the expected strings I'm looking for
        if expected_string_1 in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)
