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

try:
    from databases.pickler import Pickler as Pkl
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "pickler"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()


class Log(Command):
    """
    Outputs the lines of the log.txt file.

    LOG [/?] [/R] [/A] [text]

    /A  Appends text to the end of the log file
    /R	Output the log file in reverse (latest on top)
    /W  Wipes the log file after confirmation
    /?	Help about the Quit command
    """

    FILE_NAME = "log.txt"

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'a': self._append,
            'r': self._reverse,
            'w': self._wipe,
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):

        file_contents = Lfh.load_file_data(Lfh, self.FILE_NAME)
        direction = ""
        if len(file_contents) == 0:
            print(Err.get_error_message(208))

        Lfh.output_file(file_contents, direction)

    def _append(self):
        Lfh.append_file(self.FILE_NAME, self.user_string)
        print("Written to log: {}".format(self.user_string))

    def _reverse(self):
        file_contents = Lfh.load_file_data(Lfh, self.FILE_NAME)
        direction = "r"

        Lfh.output_file(file_contents, direction)

    def _wipe(self):
        if self.my_command_line.confirm("wipe the log"):
            Lfh.wipe_file(Lfh, self.FILE_NAME)

    def _help(self):
        print(self.__doc__)
