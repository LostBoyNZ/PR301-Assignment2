# Graham
import sys

from charts.calc_chart_data import CalcData

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from commands.command import Command
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "command"))
    sys.exit()


# Rochelle
class View(Command):
    """
    Fetches data from a file, counts the data
    and sends to the appropriate chart for output.

    VIEW /L /B /P /? [datatype]

    /L    Show line chart []
    /B  Show bar chart [bmi] or [birthday]
    /P  Show pie chart [sales] or [gender]
    /?	Help about the View command

    [datatype]
        Specifies the datatype to display the chart for
    """

    # do a prompt
    # translates switches into the method names
    # e.g. /l switch would run line chart
    def get_switch(self, switch):
        return {
            'l': self._line,
            'b': self._bar,
            'p': self._pie,
            '?': self._help
        }.get(switch, '')

    # Rochelle
    def get_data(self, choice):
        # choose file to get data from
        file_name = input("Please enter the filename to read data from >>> ")
        # check file exists
        try:
            file_contents = self._load_file_data(file_name)
            # create instance of CalcData to calc data for particular chart
            i = CalcData()

            if file_contents:  # if contents isn't empty
                if i.is_valid(file_contents):  # as long as contents are valid
                    i.calculate(file_contents,
                                choice)  # calculate the chart data
                    return i  # return i so chart can be called
                else:
                    print(Err.get_error_message(210))
        except FileNotFoundError:
            print(Err.ErrorHandler.get_error_message(201))

    # Graham
    def _load_file_data(self, file_name):
        file_contents = []
        try:
            with open(file_name, "r") as file:
                for line in file:
                    a_line = line.rstrip()
                    file_contents.append(a_line)
            file.close()
        except FileNotFoundError:
            print(Err.get_error_message(403, "requested file"))

        return file_contents

    def _default(self):
        # default is show user help
        self._help()

    def _line(self):
        # line chart for sales and salary
        if self.user_string:
            print(Err.get_error_message(102))
        else:
            valid_data = self.get_data('line')
            if valid_data:
                valid_data.line_chart()

    def _bar(self):
        # bar chart for birthday or bmi
        if self.user_string == 'bmi' or self.user_string == 'birthday':
            valid_data = self.get_data(self.user_string)
            if valid_data:
                # user string for checking which chart dat type
                valid_data.bar_chart(self.user_string)
        else:
            print(Err.get_error_message(102))

    def _pie(self):
        if self.user_string == 'sales' or self.user_string == 'gender':
            valid_data = self.get_data(self.user_string)
            if valid_data:
                valid_data.pie_chart(self.user_string)
        else:
            print(Err.get_error_message(102))

    def _help(self):
        print(self.__doc__)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
