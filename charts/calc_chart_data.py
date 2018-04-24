# Rochelle
import sys

try:
    from charts.chart_line import ChartLine
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - chart_line.py not found.")
    sys.exit()

try:
    from charts.chart_bar import ChartBar
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - chart_bar.py not found.")
    sys.exit()

try:
    from charts.chart_pie import ChartPie
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - chart_pie.py not found.")
    sys.exit()

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()


class CalcData(object):
    def __init__(self):
        # create counts for chart data
        self.count_gender_m = 0
        self.count_gender_f = 0
        self.count_bmi_ov = 0
        self.count_bmi_ob = 0
        self.count_bmi_un = 0
        self.count_bmi_no = 0
        self.count_sales_group1 = 0
        self.count_sales_group2 = 0
        self.count_sales_group3 = 0
        self.count_sales_group4 = 0
        self.count_birth_jan = 0
        self.count_birth_feb = 0
        self.count_birth_mar = 0
        self.count_birth_apr = 0
        self.count_birth_may = 0
        self.count_birth_jun = 0
        self.count_birth_jul = 0
        self.count_birth_aug = 0
        self.count_birth_sep = 0
        self.count_birth_oct = 0
        self.count_birth_nov = 0
        self.count_birth_dec = 0
        self.age_list = []
        self.salary_list = []

    # Rochelle
    # checks data inside file is correct to make a chart
    def is_valid(self, file_contents):
        """
        >>> i = CalcData()
        >>> i.is_valid("A001,gender M,age 52,sales 123,bmi Overweight,salary 50,birthday 23/10/1998,valid 1,")
        True
        >>> i.is_valid("a001,M,52,123,Overweight,50,23-10-1998 Z005,F,18,624,Normal,85,25-04-1158 C078,F,35")
        False
        >>> i.is_valid("class ErrorHandler(object):  # Claye @staticmethod def get_error_message(error_code, ")
        False
        :param file_contents:
        :return:
        """
        result = False
        try:
            values = ['gender', 'age', 'birthday', 'bmi', 'sales', 'salary']
            contents = ''.join(file_contents)
            count = 0
            for value in values:
                if value in contents:
                    count += 1
            if count == len(values):
                result = True
            return result
        except TypeError:
            return result

    def calc_line(self, key, value):
        if key == 'age':
            self.age_list += [value]
        elif key == 'salary':
            self.salary_list += [value]

    def calc_pie_gender(self, value):
        if value == 'M':
            self.count_gender_m += 1
        if value == 'F':
            self.count_gender_f += 1

    def calc_pie_sales(self, value):
        sales = int(value)
        try:
            if 0 <= sales <= 249:
                self.count_sales_group1 += 1
            elif 250 <= sales <= 499:
                self.count_sales_group2 += 1
            elif 500 <= sales <= 749:
                self.count_sales_group3 += 1
            elif 750 <= sales <= 999:
                self.count_sales_group4 += 1
        except ValueError:
            print("invalid integer")

    def calc_bar_bmi(self, value):
        if value == 'Overweight':
            self.count_bmi_ov += 1
        elif value == 'Obesity':
            self.count_bmi_ob += 1
        elif value == 'Underweight':
            self.count_bmi_un += 1
        elif value == 'Normal':
            self.count_bmi_no += 1

    # calculates number of people born in a month
    def calc_bar_birthday(self, value):
        month = value.split('/')[1]
        if month == '01':
            self.count_birth_jan += 1
        elif month == '02':
            self.count_birth_feb += 1
        elif month == '03':
            self.count_birth_mar += 1
        elif month == '04':
            self.count_birth_apr += 1
        elif month == '05':
            self.count_birth_may += 1
        elif month == '06':
            self.count_birth_jun += 1
        elif month == '07':
            self.count_birth_jul += 1
        elif month == '08':
            self.count_birth_aug += 1
        elif month == '09':
            self.count_birth_sep += 1
        elif month == '10':
            self.count_birth_oct += 1
        elif month == '11':
            self.count_birth_nov += 1
        elif month == '12':
            self.count_birth_dec += 1

    # if person has valid data
    # send to appropriate function depending on their chart choice
    def calculate(self, file_contents, choice):
        for line in file_contents[1:]:
            fields = line.split(",")
            if 'valid 1' in fields:
                for item in fields[1:-1]:
                    items = item.split(" ")
                    dict_data = {items[0]: items[1]}
                    for key, value in dict_data.items():
                        if choice == 'line':
                            self.calc_line(key, value)
                        elif key == 'gender' and choice == 'gender':
                            self.calc_pie_gender(value)
                        elif key == 'sales' and choice == 'sales':
                            self.calc_pie_sales(value)
                        elif key == 'bmi' and choice == 'bmi':
                            self.calc_bar_bmi(value)
                        elif key == 'birthday' and choice == 'birthday':
                            self.calc_bar_birthday(value)

    def line_chart(self):
        i = ChartLine()
        i.create_line_grid(self.age_list, self.salary_list)

    # depending on user chart choice add data to chart to output
    def bar_chart(self, choice):
        i = ChartBar()
        if choice == 'bmi':
            title = 'BMI'
            y_label = 'Number of Staff'
            objects = ('Obesity', 'Overweight', 'Normal', 'Underweight')
            data = [self.count_bmi_ov, self.count_bmi_ob,
                    self.count_bmi_un, self.count_bmi_no]
            fig_title = 'BMI Chart'
            i.create_bar_chart(title, y_label, objects, data, fig_title)
        elif choice == 'birthday':
            title = 'Birth Months'
            y_label = 'Number of Staff'
            objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
            data = [self.count_birth_jan, self.count_birth_feb,
                    self.count_birth_mar, self.count_birth_apr,
                    self.count_birth_may, self.count_birth_jun,
                    self.count_birth_jul, self.count_birth_aug,
                    self.count_birth_sep, self.count_birth_oct,
                    self.count_birth_nov, self.count_birth_dec]
            fig_title = 'Birth Months Chart'
            i.create_bar_chart(title, y_label, objects, data, fig_title)

    def pie_chart(self, choice):
        chart = ChartPie()
        data_labels = []
        title = ""
        window_title = ""
        data = []

        if choice == 'gender':
            data_labels = "Female", "Male"
            title = "Gender of Staff"
            window_title = "Gender Pie Graph"
            data = [self.count_gender_f, self.count_gender_m]
        elif choice == 'sales':
            data_labels = "< 250", "250 - 499", "500 - 749", "750 - 999"
            title = "Sales Brackets of Staff"
            window_title = "Sales Brackets of Staff"
            data = [self.count_sales_group1, self.count_sales_group2,
                    self.count_sales_group3, self.count_sales_group4]
        else:
            print(Err.get_error_message(601))

        if title:
            attributes = {'title': title, 'data_labels': data_labels,
                          'window_title': window_title}
            chart.create_pie_chart(data, attributes)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
