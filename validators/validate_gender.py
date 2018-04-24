# Claye
import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from validators.validator import Validator as Va
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "validator.py"))
    sys.exit()

try:
    from washers.washer import Washer as Wa
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "washer.py"))
    sys.exit()


class ValidateGender(object):
    @staticmethod
    def is_valid(to_check):
        """
        >>> ValidateGender.is_valid('male')
        ('M', True)
        >>> ValidateGender.is_valid('female')
        ('F', True)
        >>> ValidateGender.is_valid('person')
        ('Person', False)
        >>> ValidateGender.is_valid('Gi344#@$@#$rl')
        ('F', True)
        >>> ValidateGender.is_valid('')
        ('INVALID', False)
        >>> ValidateGender.is_valid('   789   ')
        ('INVALID', False)
        """

        result = False
        gender_list_m = ['M', 'Boy', 'Male', 'Dude', 'Guy']
        gender_list_f = ['F', 'Girl', 'Female', 'Lady']
        g = to_check
        g = Wa.wash_all_but_string_characters(g)
        g = Wa.set_case(g)
        if g == '':
            g = "INVALID"
        elif Va.is_in_list(g, gender_list_m):
            g = 'M'
            result = True
        elif Va.is_in_list(g, gender_list_f):
            g = 'F'
            result = True
        return g, result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
