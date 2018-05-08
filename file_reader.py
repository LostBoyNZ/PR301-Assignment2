import sys

from openpyxl import load_workbook

from data_processor import DataProcessor
from databases.database_sqlite import CompanyDatabase
from log_file_handler import LogFileHandler

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Err.py not found.")
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()

try:
    from database_excel import DatabaseExcel
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "database_excel"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()

try:
    from data_fields import DataFields
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "data_fields"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()

try:
    from file_writer import FileWriter
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "file_writer"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()


class FileReader(object):
    dict_root = {}

    def __init__(self):
        self.db = CompanyDatabase

    @staticmethod
    def get_input(text):
        return input(text)

    @staticmethod
    def fetch_workbook_file(file_name):
        return load_workbook(file_name)

    @staticmethod
    def fetch_workbook_contents(wb, switch):
        result = DatabaseExcel.get_data_from_excel(DatabaseExcel, wb, switch)
        return result

    @staticmethod
    def fetch_text_file(file_name):
        file = ""

        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(Err.get_error_message(201))

        return file

    # Claye, Works with CSV and TXT docs
    @staticmethod
    def fetch_text_contents(file, switch, separator=","):
        f = FileReader()
        dup_keys = 0
        keep_going = True
        data_fields = DataFields.get_data_fields(DataFields)

        if file is not "":
            # Repeat for each line in the text file
            for line in file:
                # Split file into fields using ","
                fields = line.split(separator)
                checked_id = DataProcessor.validate_key(fields[0])
                if checked_id in f.dict_root:
                    dup_keys += 1
                    fields[6] = fields[6].rstrip()
                    data_to_log = "Duplicate Key" + str(fields[0:])
                    LogFileHandler.append_file('log.txt', data_to_log)
                else:
                    test_dict = {}
                    field_number = 1

                    # Ignore the ID field and the Valid field for now
                    for row_name in data_fields[1:-1]:
                        test_dict[row_name] = fields[field_number]
                        field_number += 1

                    test_dict['valid'] = '0'
                    f.dict_root.update({checked_id: test_dict})

            # Close the file to free up resources (good practice)
            file.close()
            if keep_going:
                valid_dict = DataProcessor.send_to_validate(f.dict_root,
                                                            switch, dup_keys)
                return valid_dict

    def load_pickle_file(self, file_name=""):  # Claye, Graham
        file = None
        lines = ""
        if file_name == "":
            file_target = self.get_input(
                "Please input the filename to load from >>> ")
        else:
            file_target = file_name

        try:
            file = open(file_target, "rb")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        except OSError:
            print(Err.get_error_message(103))

        if file:
            with open(file_target) as file:
                lines = file.readlines()

        print(lines)
        return lines
