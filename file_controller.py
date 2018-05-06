import sys
import os

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
    from file_reader import FileReader
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "file_reader"))
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


class FileController(object):
    dict_root = {}
    file_reader = FileReader
    file_writer = FileWriter

    def call_file(self, switch, separator=','):
        valid_dict = None
        file_name = input("Please enter the filename to read data from >>> ")
        split_filename = file_name.split(".")
        file_extension = split_filename[-1]
        wb = None
        file = None
        if file_extension == "xls" or file_extension == "xlsx":
            try:
                wb = self.file_reader.fetch_workbook_file(file_name)
            except FileNotFoundError:
                print(Err.get_error_message(201))
                self.call_file(self, switch)
            except OSError:
                print(Err.get_error_message(103))
                self.call_file(self, switch)

            if wb is not None:
                data_to_save = self.file_reader.fetch_workbook_contents(wb, switch)
                FileWriter.write_file(FileWriter, data_to_save, self)
        elif file_extension == "txt" or file_extension == "csv":
            try:
                open(file_name, 'r')
            except FileNotFoundError:
                print(Err.get_error_message(201))
                self.call_file(self, switch)
            except OSError:
                print(Err.get_error_message(103))
                self.call_file(self, switch)
            else:
                file = self.file_reader.fetch_text_file(file_name)

            if file is not None:
                valid_dict = self.file_reader.fetch_text_contents(file, switch, separator)
        else:
            print(Err.get_error_message(204))

        if valid_dict:
            FileWriter.write_file(FileWriter, valid_dict, self)

    @staticmethod
    def check_path_exists(path):  # Claye
        try:
            if os.path.exists("{}".format(path)):
                return True
            else:
                return False
        except OSError:
            print(Err.get_error_message(103))