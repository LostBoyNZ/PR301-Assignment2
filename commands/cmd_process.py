# Claye

import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from commands.command import Command
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - command.py in commands folder not found.")
    sys.exit()

try:
    from file_controller import FileController
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - file_controller.py not found.")
    sys.exit()


class Process(Command):  # Claye
    """
    Fetches data from a file, validates the data
    and saves the washed data into a local file.

    PROCESS [/D] [separator]

    -D    	    Display details of data validation
    separator   Allows you to specify a custom separator

    Supported file formats include:
        .txt
        .csv
        .xlsx
        .xls
    """
    detail_mode = ""

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'd': self._detail,
            '?': self._help
        }.get(switch, '')

    # put an action here which will always run first, switch or no switch
    def _always_run(self):
        pass

    # put the default action for this class (no switches used) here
    def _default(self):
        if self.user_string:
            separator = self.user_string
        else:
            separator = ","
        i = FileController()
        FileController.call_file(i, self.detail_mode, separator)

    # put the methods for each switch here
    def _detail(self):
        self.detail_mode = "d"
        self._default()

    def _help(self):
        print(self.__doc__)
