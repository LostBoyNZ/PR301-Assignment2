# Graham

import os
import sys

_show_non_fatal_errors = True

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
    from commands.cmd_quit import Quit
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "quit"))
    pass
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_log import Log
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "log"))
    pass
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_read import Read
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "read"))
    pass
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_process import Process
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "process"))
    pass
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_pickler import Pickler
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "cmd_pickler"))
    pass
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_view import View
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "view"))
    pass
except Exception as e:
    print(Err.get_error_message(901, e))


class Help(Command):
    """
    Displays a list of supported commands.

    HELP [command]

    [command]
        Specifies the command to display help about
    """

    # translates switches into method names, /q switch would run quit
    def get_switch(self, switch):
        return {
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):

        if self.user_string != "":
            self.user_string = self.user_string.title()
            self._get_help_from_class(self.user_string)
        else:
            self._list_all_commands()

    @staticmethod
    def _list_all_commands():

        path = './commands'

        print("Supported commands: \n")

        for root, dirs, files in os.walk(path):
            for filename in files:
                split_filename = filename.split(".", 1)
                if split_filename[0].startswith("cmd_") and \
                        split_filename[1].endswith("py"):
                    # Hide the cmd_ from the start of the file name
                    filename = split_filename[0]
                    filename = filename[4:]
                    filename = filename.upper()
                    print(filename)

        print("\nFor information on specific commands, type HELP command-name")

    @staticmethod
    def _get_help_from_class(class_to_call):
        try:
            class_name = getattr(sys.modules[__name__], class_to_call)
            print(class_name.__doc__)
        except AttributeError:
            print(
                "The command '{}' is not found.".format(class_to_call))

    def _help(self):
        print(self.__doc__)
