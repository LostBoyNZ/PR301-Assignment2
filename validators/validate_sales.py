# Rochelle

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


class ValidateSales(object):
    def __init__(self):
        self.min_sales = 0
        self.min_length = 3
        self.max_length = 3

    def is_valid(self, sales):
        """
        >>> i = ValidateSales()
        >>> i.is_valid("780")
        ('780', True)
        >>> i.is_valid(7800)
        ('7800', False)
        >>> i.is_valid('  RFGVHJ#$%^&*  67       @#$%^&*(DFGHJ')
        ('067', True)
        >>> i.is_valid(' twenty-two ')
        (' twenty-two ', False)
        :param sales:
        :return:
        """
        result = False
        try:
            if isinstance(sales, int):
                sales = Wa.to_string(sales, self.min_length)
                if Va.is_minimum(sales, self.min_sales):
                    result = Va.is_within_length(self.min_length,
                                                 self.max_length, str(sales))
            elif isinstance(int(Wa.keep_only_nums(sales)), int):
                if Wa.strip_string(sales):
                    sales = Wa.keep_only_nums(sales)
                    sales = Wa.to_string(sales, self.min_length)
                    if Va.is_minimum(sales, self.min_sales):
                        result = Va.is_within_length(self.min_length,
                                                     self.max_length,
                                                     str(sales))
            else:
                result = False
            return sales, result
        except ValueError:
            result = False
            return sales, result
