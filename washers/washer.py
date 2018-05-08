import re


class Washer(object):
    # Graham
    # For example calling:
    #   keep_only_these_in_string("jun99", "a-z")
    # Returns:
    #   "jun"
    #
    # Because it only keeps letters a-z
    # a-zA-Z0-9 would keep all letters and numbers

    @staticmethod
    def keep_only_these_in_string(regex_to_keep, data):
        regex_target = re.compile(r"[^" + regex_to_keep + "]")

        new_data = regex_target.sub("", data)
        return new_data

    # Graham
    # Output will have one capital letter then all lowercase
    # e.g. tEsT would become Test
    @staticmethod
    def set_case(data):
        """
        >>> Washer.set_case(testingng')
        'Test'
        >>> Washer.set_case('TEST')
        'Test'
        """
        new_data = data.title()

        return new_data

    # Graham
    # For example calling:
    #   replace_x_with_y("-", "/")
    # Would change 10-01-1998 to 10/01/1998
    @staticmethod
    def replace_x_with_y(x, y, data):
        """
        >>> Washer.replace_x_with_y('-','/', '-/-')
        '///'
        """
        target = x
        replacement = y

        new_data = re.sub(target, replacement, data)

        return new_data

    @staticmethod  # Claye
    def wash_all_but_string_characters(to_wash):
        to_wash = ''.join([c for c in to_wash if c not in " 1234567890"])
        to_wash = re.sub(r'[^\w]', '', to_wash)

        return to_wash

    # Rochelle
    @staticmethod
    def keep_only_nums(data):
        keep = re.compile(r"[^0-9]")
        data = keep.sub("", data)
        data = data.strip()
        return data

    # Rochelle
    @staticmethod
    def strip_string(data):
        data = data.lstrip()
        data = data.rstrip()
        return data

    # Rochelle
    @staticmethod
    def to_string(data, min_length):
        if 0 < len(str(data)) < min_length:
            i = ''
            for num in range(0, min_length - len(str(data))):
                i += '0'
            data = i + str(data)
        else:
            data = str(data)
        return data


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
