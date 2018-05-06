import sys
import os

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
    from database_excel import DatabaseExcel as Dbexel
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

    def call_file(self, switch, separator):
        file_name = input("Please enter the filename to read data from >>> ")
        split_filename = file_name.split(".")
        file_extension = split_filename[-1]
        if file_extension == "xls" or file_extension == "xlsx":
            try:
                wb = load_workbook(file_name)
            except FileNotFoundError:
                print(Err.get_error_message(201))
                self.call_file(switch)
            except OSError:
                print(Err.get_error_message(103))
                self.call_file(switch)

            i = Dbexel()
            data_to_save = i.create_connection(wb, switch)
            FileWriter.write_file(data_to_save)
        elif file_extension == "txt" or file_extension == "csv":
            try:
                valid_dict = self.split_file(file_name, switch, separator)
                print(valid_dict)
            except FileNotFoundError:
                print(Err.get_error_message(201))
                self.call_file(switch)
            except OSError:
                print(Err.get_error_message(103))
                self.call_file(switch)
        else:
            print(Err.get_error_message(204))

        if valid_dict:
            FileWriter.write_file(valid_dict)

    # Claye, Works with CSV and TXT docs
    def split_file(self, file_name, switch, separator=","):
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        else:
            # Repeat for each line in the text file
            f = FileReader()
            dup_keys = 0
            keep_going = True
            data_fields = DataFields.get_data_fields(DataFields)

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

    def load_pickle_file(self):  # Claye, Graham
        file_target = input("Please input the filename to load from >>> ")
        try:
            file = open(file_target, "rb")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        except OSError:
            print(Err.get_error_message(103))

        with open(file_target) as file:
            lines = file.readlines()

        print(lines)
        return lines

    @staticmethod
    def check_path_exists(path):  # Claye
        result = False
        try:
            if os.path.exists("{}".format(path)):
                result = True
                return result
            else:
                return result
        except OSError:
            print(Err.get_error_message(103))
