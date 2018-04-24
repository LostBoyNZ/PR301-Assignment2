# Graham

import sys
from datetime import datetime

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


class ValidateDate:  # Graham

    @staticmethod
    def split_string(delimiter, data):
        """
        >>> ValidateDate.split_string('/', '1/1/1998')
        ['1', '1', '1998']
        """
        return data.split(delimiter)

    def add_zeros(self, data):
        try:
            split_date = self.split_string("/", data)
            day = split_date[0]
            month = split_date[1]
            year = split_date[2]

            if day.isdigit():
                day = day.zfill(2)
            if month.isdigit():
                month = month.zfill(2)

            output = day + "/" + month + "/" + year
        except IndexError:
            output = data

        return output

    @staticmethod
    def is_real_date(data, date_format):
        """
        >>> ValidateDate.is_real_date('01/01/1998', '%d/%m/%Y')
        True
        >>> ValidateDate.is_real_date('32/01/1998', '%d/%m/%Y')
        False
        """
        result = False

        try:
            datetime.strptime(data, date_format)
            result = True
        except ValueError:
            result = False

        return result

    def determine_month_format(self, data):
        # default to number format like 09 for September
        result = "%m"

        date_to_check = Wa.replace_x_with_y("\W+", "/", data)
        split_date = self.split_string("/", date_to_check)
        for value in split_date:
            if value.isalpha():
                if len(value) > 3:
                    result = "%B"
                else:
                    result = "%b"

        return result

    def month_string_to_number(self, data):

        date_to_check = Wa.replace_x_with_y("\W+", "/", data)
        split_date = self.split_string("/", date_to_check)
        for value in split_date:
            if value.isalpha():
                if len(value) > 3:
                    # result = "%B"
                    text_month = datetime.strptime(value, '%B')
                    split_date[1] = text_month.strftime('%m')
                else:
                    # result = "%b"
                    text_month = datetime.strptime(value, '%b')
                    split_date[1] = text_month.strftime('%m')

        output = ""
        try:
            output = split_date[0] + "/" + split_date[1] + "/" + split_date[2]
        except IndexError:
            pass

        return output

    def determine_date_format(self, data):
        day_format = "%d"
        month_format = self.determine_month_format(data)
        year_format = "%Y"
        format = day_format + " " + month_format + " " + year_format

        return format

    def wash_data(self, data_to_wash):
        # replace any non-word character with a forward slash
        data_to_wash = Wa.replace_x_with_y("\W+", "/", data_to_wash)
        # remove st, nd and rd from date, e.g. 21st, 22nd, 23rd
        data_to_wash = Wa.replace_x_with_y("st|nd|rd", "", data_to_wash)
        data_to_wash = self.month_string_to_number(data_to_wash)

        return data_to_wash

    def is_valid(self, data_to_validate):
        result = False

        data_to_validate = data_to_validate.lstrip(' ')

        # If there's no numbers in string, just return as is, it's bad data
        if Va.has_this_many_numbers(0, data_to_validate):
            date_output = data_to_validate
        else:
            washed_data = self.wash_data(data_to_validate)

            # add zeros if needed
            washed_data = self.add_zeros(washed_data)

            # remove all spaces
            washed_data = washed_data.strip()

            date_format = self.determine_date_format(washed_data)
            date_to_check = Wa.replace_x_with_y('\W+', " ", washed_data)
            result = self.is_real_date(date_to_check, date_format)

            date_output = Wa.replace_x_with_y(" ", "/", date_to_check)

        return date_output, result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
