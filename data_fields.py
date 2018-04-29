import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Err.py not found.")
    sys.exit()


class DataFields:
    FILE_NAME = "database_fields.txt"

    def open_file(self):
        file = None

        try:
            file = open(self.FILE_NAME)
        except FileNotFoundError or OSError:
            print(Err.get_error_message(404, self.FILE_NAME))
            sys.exit()
        except:
            print(Err.get_error_message(406, self.FILE_NAME))
            sys.exit()

        return file

    @staticmethod
    def split_data(data_to_split):
        return data_to_split.split(",")

    def get_data_fields(self):
        data_fields_list = []

        file = self.open_file(self)

        if file is not None:
            file_contents = file.readline()
            split_file_contents = self.split_data(file_contents)

            for field in split_file_contents:
                data_fields_list.append(field.strip())

        return data_fields_list
