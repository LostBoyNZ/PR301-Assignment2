# Graham
import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()
except Exception as e:
    print("Exception: {}".format(e))
    sys.exit()

class LogFileHandler(object):
    # set to read a file by default
    def open_file(self, file_name, mode='r'):
        file = ""
        try:
            file = open(file_name, mode)
        except FileNotFoundError:
            try:
                print(Err.get_error_message(403, "log"))
                print("Creating log file...")
                self._create_file(self, file_name)
            except OSError:
                print(Err.get_error_message(401, "log"))
            except:
                print(Err.get_error_message(402, "log"))
            else:
                print("log.txt file created")

        return file

    @staticmethod
    def close_file(file):
        file.close()

    def load_file_data(self, file_name):
        file_contents = []
        try:
            with self.open_file(self, file_name, "r") as file:
                for line in file:
                    a_line = line.rstrip()
                    file_contents.append(a_line)
            self.close_file(file)
        except FileNotFoundError:
            try:
                print(Err.get_error_message(403, "log"))
                print("Creating log file...")
                self._create_file(self, file_name)
            except OSError:
                print(Err.get_error_message(401, "log"))
            except:
                print(Err.get_error_message(402, "log"))
            else:
                print("log.txt file created")
        return file_contents

    def file_is_empty(self, file_name):
        result = False

        file_contents = self.load_file_data(file_name)

        if len(file_contents) == 0:
            result = True

        return result

    def wipe_file(self, file_name):
        try:
            file = self.open_file(self, file_name, "r+")
            file.truncate()
            self.close_file(file)
        except PermissionError:
            print(Err.get_error_message(405, "log"))

        if self.file_is_empty(file_name):
            print("Log file wiped")
        else:
            print("Log file not wiped")

    def _create_file(self, file_name):
        file = self.open_file(self, file_name, "w+")
        self.close_file(file)

    @staticmethod
    def output_file(file_contents, direction):
        if file_contents:
            if direction == "r":
                for line in file_contents[::-1]:
                    print(line)
            else:
                for line in file_contents:
                    print(line)

    def get_log(self, file_name):
        file_contents = self.load_file_data(self, file_name)
        output = []

        for line in file_contents:
            output.append(line)
        print(output)
        return output

    def set_log(self, file_name, data_to_write):
        self.wipe_file(file_name)

        file = open(file_name, "a+")

        for line in data_to_write:
            file.write(line + "\n")

        file.close()

    @staticmethod
    def append_file(file_name, data_to_write):
        file = open(file_name, "a+")
        file.write(data_to_write + "\n")
        file.close()
