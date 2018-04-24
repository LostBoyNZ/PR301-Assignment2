# Graham

import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()
except Exception as e:
    print("Exception: {}".format(e))
    sys.exit()

try:
    from commands.command import Command
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "command"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()

try:
    from log_file_handler import LogFileHandler as Lfh
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "log_file_handler"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()


class Read(Command):
    """
    Outputs a text file, and prompts for a file name if not provided in command

    READ [/?] [filename]

    /?	Help about the Quit command
    """

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):
        direction = ""

        if self.user_string:
            file_name = self._check_file_name(self.user_string)
        else:
            file_name = self._request_file_name()

        if file_name:
            self._read_file(file_name, direction)

    def _help(self):
        print(self.__doc__)

    def _request_file_name(self):
        output = ""

        file_name = input(
            "Please enter the .txt filename to read data from >>> ")
        if file_name:
            output = self._check_file_name(file_name)

        return output

    @staticmethod
    def _check_file_name(file_name):
        output = ""

        split_filename = file_name.split(".")
        file_extension = split_filename[-1]
        if file_extension == "txt":
            output = file_name

        return output

    def _read_file(self, file_name, direction):
        file_contents = ""

        if file_name:
            try:
                file_contents = open(file_name, "r")
            except FileNotFoundError:
                print(Err.get_error_message(201))
            except OSError:
                print(Err.get_error_message(102))
            except Exception as e:
                print(Err.get_error_message(901, e))

            Lfh.output_file(file_contents, direction)
        else:
            print(Err.get_error_message(204))
