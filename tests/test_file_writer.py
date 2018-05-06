import io
import sys
from pickle import dumps
import pickle
from file_writer import FileWriter
from unittest.mock import patch
import unittest
import string
import random


class TestFileReader(unittest.TestCase):

    def test_write_to_database_with_valid_data(self):
        # Arrange
        user_input = ['Y']
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996', 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        data_to_test = {'A001': line1, 'T991': line2}
        expected_string_1 = "['A001', 'F,', '21,', '001,', 'Normal,', '12,'," \
                            " '01/01/1996,', '1']"
        expected_string_2 = "['T991', 'M,', '45,', '999,', 'Underweight,'," \
                            " '725,', '31/12/1971,', '1']"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileWriter.write_to_database(FileWriter, data_to_test)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_string_1 in captured_output.getvalue()\
                and expected_string_2 in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)

    def test_save_pickle_file(self):
        # Arrange
        file_name = "testdata\\test_pickle_save.txt"
        data_to_save = "This is being saved to a file"

        # Act
        pickled = dumps(data_to_save)
        FileWriter.commit_pickle_save(file_name, pickled)    # Pickle

        # Open the file it just saved
        with open(file_name, 'rb') as pickleFile:
            result = pickle.load(pickleFile)
        pickleFile.close()

        # Assert
        self.assertTrue(data_to_save == result)

    @patch('file_writer.FileWriter.get_input', return_value='Y')
    def test_save_pickle_file_yes_saves_file(self, input):
        # Arrange
        data_to_save = "Something to pickle"
        pickled = dumps(data_to_save)

        # Act
        FileWriter.save_pickle_file(FileWriter, pickled)

        # Open the file it just saved, called Y because I can only submit
        # the same input to every request for input
        with open("Y", 'rb') as pickleFile:
            result = pickle.load(pickleFile)
        pickleFile.close()

        # Assert
        self.assertTrue(data_to_save == result)

    @patch('file_writer.FileWriter.get_input', return_value='N')
    def test_save_pickle_file_no_does_not_save_file(self, input):
        # Arrange
        data_to_save = "Something to pickle"
        pickled = dumps(data_to_save)

        # Act
        FileWriter.save_pickle_file(FileWriter, pickled)

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
        file_name = "testdata\\test_pickle_save.txt"
        data_to_save = "This is being saved to a file"
        expected_data_loaded = "This is being saved to a file"
        pickled = dumps(data_to_save)

        # Act
        FileWriter.commit_pickle_save(file_name, pickled)

        # Open the file it just saved
        with open(file_name, 'rb') as pickleFile:
            result = pickle.load(pickleFile)
        pickleFile.close()

        # Assert
        self.assertTrue(data_to_save == result)

    def test_commit_save(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001',
                 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        file_target = "testdata\\test_file_to_write_to.txt"
        ids_already_in_file = []
        expected_output = "File saved, 2 rows added"

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileWriter.commit_save(dict_valid, file_target, ids_already_in_file)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_commit_save_with_one_duplicate_key(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996', 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        file_target = "testdata\\test_file_to_write_to.txt"
        ids_already_in_file = ['A001']
        expected_output\
            = "1 of 2 rows were duplicate keys and not inserted again"

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileWriter.commit_save(dict_valid, file_target, ids_already_in_file)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_commit_save_with_all_duplicate_keys(self):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001',
                 'bmi': 'Normal', 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        file_target = "testdata\\test_file_to_write_to.txt"
        ids_already_in_file = ['A001', 'Q001']
        expected_output\
            = "All ID's already existed in the output file. Nothing added."

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        FileWriter.commit_save(dict_valid, file_target, ids_already_in_file)
        sys.stdout = sys.__stdout__

        # Check if the printed output includesexpected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    @patch('file_writer.FileWriter.get_input', return_value='Y')
    def test_write_file(self, input):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}
        open("Y", 'w').close()      # Wipe the file for a fresh start

        # Act
        FileWriter.write_file(FileWriter, dict_valid)

        # Open the file it just saved
        with open("Y", 'rb') as file:
            result = file
        file.close()

        # Assert
        self.assertTrue(file)

    @patch('file_writer.FileWriter.get_input', return_value='N')
    def test_write_file_do_not_write(self, input):
        # Arrange
        line1 = {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal',
                 'salary': '12', 'birthday': '01/01/1996',
                 'valid': '1'}
        line2 = {'gender': 'M', 'age': '45', 'sales': '999',
                 'bmi': 'Underweight', 'salary': '725',
                 'birthday': '31/12/1971', 'valid': '1'}
        dict_valid = {'A001': line1, 'Q001': line2}

        # Act
        FileWriter.write_file(FileWriter, dict_valid)

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
        user_input = ['Y', 'F', "testdata\\file_already_exists.txt", "N", "Y",
                      "F", "testdata\\new.txt", "Y"]
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001',
                               'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_result = ['This file already exists']

        # Act
        with patch('builtins.input', side_effect=user_input):
            FileWriter.write_file(FileWriter, dict_valid)

        # Assert
        file = open('testdata\\file_already_exists.txt')
        result = []
        for line in file:
            result.append(line)
        file.close()

        self.assertTrue(result == expected_result)

    def test_write_file_new_file(self):
        # Arrange
        random_file_name = ''.join(random.sample(string.ascii_lowercase, 8))
        random_file_name = "temp\\" + random_file_name + ".txt"
        user_input = ['Y', 'F', random_file_name]
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001',
                               'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_result = ['\n', 'A001,gender F,age 21,sales 001,bmi Normal,'
                                 'salary 12,birthday 01/01/1996,valid 1,\n']

        # Act
        with patch('builtins.input', side_effect=user_input):
            FileWriter.write_file(FileWriter, dict_valid)

        # Assert
        file = open(random_file_name)
        result = []
        for line in file:
            result.append(line)
        file.close()

        self.assertTrue(result == expected_result)

    def test_write_file_invalid_input(self):
        # Arrange
        user_input = ['Z']
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001',
                               'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_output = "Invalid Input, please try again"

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileWriter.write_file(FileWriter, dict_valid)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_output in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result)

    def test_write_file_choosing_database_option(self):
        # Arrange
        user_input = ['Y', "D", "Y"]
        dict_valid = {'A001': {'gender': 'F', 'age': '21', 'sales': '001',
                               'bmi': 'Normal', 'salary': '12',
                      'birthday': '01/01/1996', 'valid': '1'}}
        expected_string = "['A001', 'F,', '21,', '001,', 'Normal,', '12,'," \
                            " '01/01/1996,', '1']"
        expected_result = True

        # Act
        captured_output = io.StringIO()
        sys.stdout = captured_output
        with patch('builtins.input', side_effect=user_input):
            FileWriter.write_file(FileWriter, dict_valid)
        sys.stdout = sys.__stdout__

        # Check if the printed output includes expected strings I'm looking for
        if expected_string in captured_output.getvalue():
            result = True
        else:
            result = False

        # Assert
        self.assertTrue(result == expected_result)
