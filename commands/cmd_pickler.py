# Graham, Claye

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

try:
    from file_reader import FileReader as fr
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "file_reader"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()


class Pickler(Command):  # Graham, Claye
    """
    Pickles or un-pickles

    PICKLER [D] [P] [U] [?] [data]

    /D  Display detail on data
    /P  Pickle data
    /U  Unpickle data
    /?  Help

    [data]
        Specifies either [log] or [errors] as the data to use
    """
    pickled_log = []
    pickled_errors = []
    display_detail_output = False

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'd': self._display_output,
            'p': self._pickle,
            'u': self._unpickle,
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):
        print(self.__doc__)

    def _pickle(self):
        if self.user_string == "log":
            self._pickle_log()
        if self.user_string == "error" or self.user_string == "errors":
            self._pickle_errors()

    def _unpickle(self):
        if self.user_string == "log":
            self._unpickle_log()
        if self.user_string == "error" or self.user_string == "errors":
            self._unpickle_errors()

    def _help(self):
        print(self.__doc__)

    def _display_output(self):
        self.display_detail_output = True

    def _pickle_log(self):
        data_to_pickle = Lfh.get_log(Lfh, "log.txt")
        pickled_data = Pkl.pickle_data(data_to_pickle)
        self.pickled_log.append(pickled_data)
        if self.display_detail_output:
            print("Input: {}".format(data_to_pickle))
            print("Pickled Data: {}".format(self.pickled_log))

    def _unpickle_log(self):
        un_pickled_data = ""

        try:
            un_pickled_data = Pkl.unpickle_data(self.pickled_log[0])
        except IndexError:
            print(Err.get_error_message(208))
        if self.display_detail_output:
            print("Unpickled Data: {}".format(un_pickled_data))

        return un_pickled_data

    def _pickle_errors(self):
        pickled_data = Err.send_data_to_pickler()
        self.pickled_errors.append(pickled_data)
        if self.display_detail_output:
            print("Pickled Data: {}".format(pickled_data))

    def _unpickle_errors(self):
        un_pickled_data = ""

        try:
            un_pickled_data = Pkl.unpickle_data(self.pickled_errors[0])
        except IndexError:
            print(Err.get_error_message(208))
        if self.display_detail_output:
            print("Unpickled Data: {}".format(un_pickled_data))
        return un_pickled_data
