import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()
except Exception as e:
    print("Exception: {}".format(e))
    sys.exit()

class Command:
    my_command_line = None
    user_string = ""

    def __init__(self, switches_and_data, command_line):
        if __name__ == "__main__":
            pass
        else:
            self.go(switches_and_data, command_line)

    def go(self, switches_and_data, command_line):
        self.my_command_line = command_line
        has_switches = False

        # extract and run switch methods and extract user data
        # e.g. file name, from the command
        if switches_and_data:
            methods_to_run, self.user_string = self.get_switch_and_data(
                switches_and_data, self)
            if methods_to_run:
                self._run_switch_methods(methods_to_run)
                has_switches = True

        if not has_switches:
            self._default()

    def _run_switch_methods(self, methods_to_run):
        for method in methods_to_run:
            try:
                method()
            except TypeError:
                pass
            except Exception as e:
                print(Err.get_error_message(901, e))

    def get_switch_and_data(self, user_data, my_command):
        methods_to_run = []
        strings_to_keep = []
        split_user_data = user_data.split(" ")

        for data in split_user_data:
            try:
                if data[0] == "/" and len(data) == 2:
                    switch = my_command.get_switch(data[1])
                    methods_to_run.append(switch)
                    if switch == "":
                        print(Err.get_error_message(105))
                else:
                    not_a_switch = data
                    strings_to_keep.append(not_a_switch)
            except IndexError:
                pass
            except Exception as e:
                print(Err.get_error_message(901, e))

        user_string = " ".join(strings_to_keep)
        return methods_to_run, user_string
