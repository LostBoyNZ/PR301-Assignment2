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


class Quit(Command):
    """
    Exits the software with a prompt to confirm.

    QUIT [/?] [/Q]

    /Q	Quiet mode disables the confirmation prompt
    /?	Help about the Quit command
    """

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'q': self._quit,
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):
        if self.my_command_line.confirm("quit"):
            self._quit()

    # put the methods for each switch here
    def _quit(self):
        sys.exit()

    def _help(self):
        print(self.__doc__)
