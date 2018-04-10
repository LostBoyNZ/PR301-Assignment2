# Graham

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
    from views.console_view import ConsoleView as cv
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "console_view"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_quit import Quit
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "quit"))
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_help import Help
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "help"))
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_log import Log
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "log"))
except Exception as e:
    print(Err.get_error_message(901, e))


try:
    from commands.cmd_read import Read
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "read"))
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_pickler import Pickler
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "cmd_pickler"))
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from commands.cmd_process import Process
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "process"))
except Exception as e:
    print(Err.get_error_message(901, e))
try:
    from commands.cmd_view import View
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(Err.get_error_message(403, "view"))
except Exception as e:
    print(Err.get_error_message(901, e))


class CommandLine:
    prompt = ""  # Rochelle
    user_name = ""
    debug_mode = False

    def __init__(self):
        self.prompt = "> "
        if self.debug_mode:
            self.prompt = "debug > "

    def run_commandline(self, user_args):
        self._handle_args(user_args)
        if self.user_name:
            self._greet_user()
        while True:
            self._get_command()

    def _handle_args(self, user_args):
        if len(user_args) > 0:  # Graham
            self.user_name = user_args[0]   # Graham
        if len(user_args) > 1:
            if user_args[1].upper() == '/D':  # Claye
                self.debug_mode = True  # Claye
                self.prompt = "debug > "
        if len(user_args) > 2:
            self.prompt = user_args[2]  # Rochelle

    def _greet_user(self):  # Graham
        cv.show_output("Welcome " + self.user_name)

    def _get_command(self):
        user_command = cv.get_input(self.prompt)
        self._split_command(user_command)

    def _split_command(self, user_command):
        switches_and_data = ""

        # split the command at the start, from the entire string
        split_input = user_command.split(" ", 1)
        # capitalize the command as that's a class name to call
        class_to_call = split_input[0].title()

        # if there's any more, that's switches and user data, e.g. a file name
        if len(split_input) > 1:
            switches_and_data = split_input[1].lower()

        self._process_command(class_to_call, switches_and_data)

    def _process_command(self, class_to_call, switches_and_data):
        if class_to_call:
            if self.debug_mode is False:
                try:
                    class_name = getattr(sys.modules[__name__], class_to_call)
                    class_name(switches_and_data, self)
                except AttributeError:
                    cv.show_output(
                        "The command '{}' is not valid. Enter"
                        " 'Help' for a list of commands"""
                        .format(class_to_call))
                except Exception as e:
                    print(Err.get_error_message(104, e))
            else:
                class_name = getattr(sys.modules[__name__], class_to_call)
                class_name(switches_and_data, self)

    def confirm(self, action_name):
        result = False
        prompt = "Are you sure you want to {}? Y/N".format(action_name)
        user_input = cv.get_input(prompt)

        try:
            if user_input[0].lower() == "y":
                result = True
        except IndexError:
            print(Err.get_error_message(102))
            self.confirm(action_name)
        except Exception as e:
            print(Err.get_error_message(104, e))

        return result
