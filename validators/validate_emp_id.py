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
    from validators.validator import Validator as Va
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "validator.py"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from washers.washer import Washer as Wa
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "washer.py"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))


class ValidateEmpId:
    @staticmethod
    def is_valid(data_to_validate):
        correct_length = False
        correct_number_of_characters = False
        correct_characters = False
        correct_format = False

        # Wash the data before verifying it
        washed_data = Wa.keep_only_these_in_string("a-zA-Z0-9",
                                                   data_to_validate)
        washed_data = Wa.set_case(washed_data)

        # \D where a non-number should be, and \d where a number should be
        if Va.is_correct_pattern("\D\d\d\d", washed_data):
            correct_format = True

        if Va.is_within_length(4, 4, washed_data) :
            correct_length = True

        if Va.has_this_many_numbers(3, washed_data)  \
                and Va.has_this_many_letters(1, washed_data) :
            correct_number_of_characters = True

        if washed_data.isalnum() :
            correct_characters = True

        is_valid = correct_length and correct_number_of_characters and\
                   correct_characters and correct_format

        return washed_data, is_valid
