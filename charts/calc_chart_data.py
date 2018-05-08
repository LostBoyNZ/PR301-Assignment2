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

    def get_count_gender_m(self):
        return self.count_gender_m

    def get_count_gender_f(self):
        return self.count_gender_f

    def get_count_bmi_ov(self):
        return self.count_bmi_ov

    def get_count_bmi_ob(self):
        return self.count_bmi_ob

    def get_count_bmi_un(self):
        return self.count_bmi_un

    def get_count_bmi_no(self):
        return self.count_bmi_no

    def get_count_sales_group1(self):
        return self.count_sales_group1

    def get_count_sales_group2(self):
        return self.count_sales_group2

    def get_count_sales_group3(self):
        return self.count_sales_group3

    def get_count_sales_group4(self):
        return self.count_sales_group4

    def get_count_birth_jan(self):
        return self.count_birth_jan

    def get_count_birth_feb(self):
        return self.count_birth_feb

    def get_count_birth_mar(self):
        return self.count_birth_mar

    def get_count_birth_apr(self):
        return self.count_birth_apr

    def get_count_birth_may(self):
        return self.count_birth_may

    def get_count_birth_jun(self):
        return self.count_birth_jun

    def get_count_birth_jul(self):
        return self.count_birth_jul

    def get_count_birth_aug(self):
        return self.count_birth_aug

    def get_count_birth_sep(self):
        return self.count_birth_sep

    def get_count_birth_oct(self):
        return self.count_birth_oct

    def get_count_birth_nov(self):
        return self.count_birth_nov

    def get_count_birth_dec(self):
        return self.count_birth_dec

    def get_age_list(self):
        return self.age_list

    def get_salary_list(self):
        return self.salary_list

    def set_count_gender_m(self, new_data):
        self.count_gender_m = new_data

    def set_count_gender_f(self, new_data):
        self.count_gender_f = new_data

    def set_count_bmi_ov(self, new_data):
        self.count_bmi_ov = new_data

    def set_count_bmi_ob(self, new_data):
        self.count_bmi_ob = new_data

    def set_count_bmi_un(self, new_data):
        self.count_bmi_un = new_data

    def set_count_bmi_no(self, new_data):
        self.count_bmi_no = new_data

    def set_count_sales_group1(self, new_data):
        self.count_sales_group1 = new_data

    def set_count_sales_group2(self, new_data):
        self.count_sales_group2 = new_data

    def set_count_sales_group3(self, new_data):
        self.count_sales_group3 = new_data

    def set_count_sales_group4(self, new_data):
        self.count_sales_group4 = new_data

    def set_count_birth_jan(self, new_data):
        self.count_birth_jan = new_data

    def set_count_birth_feb(self, new_data):
        self.count_birth_feb = new_data

    def set_count_birth_mar(self, new_data):
        self.count_birth_mar = new_data

    def set_count_birth_apr(self, new_data):
        self.count_birth_apr = new_data

    def set_count_birth_may(self, new_data):
        self.count_birth_may = new_data

    def set_count_birth_jun(self, new_data):
        self.count_birth_jun = new_data

    def set_count_birth_jul(self, new_data):
        self.count_birth_jul = new_data

    def set_count_birth_aug(self, new_data):
        self.count_birth_aug = new_data

    def set_count_birth_sep(self, new_data):
        self.count_birth_sep = new_data

    def set_count_birth_oct(self, new_data):
        self.count_birth_oct = new_data

    def set_count_birth_nov(self, new_data):
        self.count_birth_nov = new_data

    def set_count_birth_dec(self, new_data):
        self.count_birth_dec = new_data

    def set_age_list(self, new_data):
        self.age_list = new_data

    def set_salary_list(self, new_data):
        self.salary_list = new_data

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
            new_age_list = self.get_age_list()
            new_age_list += [value]
            self.set_age_list(new_age_list)
        elif key == 'salary':
            new_data = self.get_salary_list()
            new_data += [value]
            self.set_salary_list(new_data)

    def calc_pie_gender(self, value):
        if value == 'M':
            new_data = self.get_count_gender_m()
            new_data += 1
            self.set_count_gender_m(new_data)
        if value == 'F':
            new_data = self.get_count_gender_f()
            new_data += 1
            self.set_count_gender_f(new_data)

    def calc_pie_sales(self, value):
        sales = int(value)
        try:
            if 0 <= sales <= 249:
                new_data = self.get_count_sales_group1()
                new_data += 1
                self.set_count_sales_group1(new_data)
            elif 250 <= sales <= 499:
                new_data = self.get_count_sales_group2()
                new_data += 1
                self.set_count_sales_group2(new_data)
            elif 500 <= sales <= 749:
                new_data = self.get_count_sales_group3()
                new_data += 1
                self.set_count_sales_group3(new_data)
            elif 750 <= sales <= 999:
                new_data = self.get_count_sales_group4()
                new_data += 1
                self.set_count_sales_group4(new_data)
        except ValueError:
            print("invalid integer")

    def calc_bar_bmi(self, value):
        if value == 'Overweight':
            new_data = self.get_count_bmi_ov()
            new_data += 1
            self.set_count_bmi_ov(new_data)
        elif value == 'Obesity':
            new_data = self.get_count_bmi_ob()
            new_data += 1
            self.set_count_bmi_ob(new_data)
        elif value == 'Underweight':
            new_data = self.get_count_bmi_un()
            new_data += 1
            self.set_count_bmi_un(new_data)
        elif value == 'Normal':
            new_data = self.get_count_bmi_no()
            new_data += 1
            self.set_count_bmi_no(new_data)

    # calculates number of people born in a month
    def calc_bar_birthday(self, value):
        month = value.split('/')[1]
        if month == '01':
            new_data = self.get_count_birth_jan()
            new_data += 1
            self.set_count_birth_jan(new_data)
        elif month == '02':
            new_data = self.get_count_birth_feb()
            new_data += 1
            self.set_count_birth_feb(new_data)

        elif month == '03':
            new_data = self.get_count_birth_mar()
            new_data += 1
            self.set_count_birth_mar(new_data)

        elif month == '04':
            new_data = self.get_count_birth_apr()
            new_data += 1
            self.set_count_birth_apr(new_data)

        elif month == '05':
            new_data = self.get_count_birth_may()
            new_data += 1
            self.set_count_birth_may(new_data)

        elif month == '06':
            new_data = self.get_count_birth_jun()
            new_data += 1
            self.set_count_birth_jun(new_data)

        elif month == '07':
            new_data = self.get_count_birth_jul()
            new_data += 1
            self.set_count_birth_jul(new_data)

        elif month == '08':
            new_data = self.get_count_birth_aug()
            new_data += 1
            self.set_count_birth_aug(new_data)

        elif month == '09':
            new_data = self.get_count_birth_sep()
            new_data += 1
            self.set_count_birth_sep(new_data)

        elif month == '10':
            new_data = self.get_count_birth_oct()
            new_data += 1
            self.set_count_birth_oct(new_data)

        elif month == '11':
            new_data = self.get_count_birth_nov()
            new_data += 1
            self.set_count_birth_nov(new_data)

        elif month == '12':
            new_data = self.get_count_birth_dec()
            new_data += 1
            self.set_count_birth_dec(new_data)


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
            title = "BMI"
            fig_title = 'BMI Chart'
            y_label = "Number of Staff"
            data_labels = ['Obesity', 'Overweight', 'Normal', 'Underweight']
            output_file_name = 'created_charts\\bar_chart.png'

            ChartBar.set_title(ChartBar, title)
            ChartBar.set_y_label(ChartBar, y_label)
            ChartBar.set_labels(ChartBar, data_labels)
            ChartBar.set_fig_title(ChartBar, fig_title)

            data = [self.get_count_bmi_ov(), self.get_count_bmi_ob(),
                    self.get_count_bmi_un(), self.get_count_bmi_no()]
            ChartBar.create_bar_chart(ChartBar, data, output_file_name)
        elif choice == 'birthday':
            title = 'Birth Months'
            y_label = 'Number of Staff'
            data_labels = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
            data = [self.get_count_birth_jan(), self.get_count_birth_feb(),
                    self.get_count_birth_mar(), self.get_count_birth_apr(),
                    self.get_count_birth_may(), self.get_count_birth_jun(),
                    self.get_count_birth_jul(), self.get_count_birth_aug(),
                    self.get_count_birth_sep(), self.get_count_birth_oct(),
                    self.get_count_birth_nov(), self.get_count_birth_dec()]
            fig_title = 'Birth Months Chart'
            output_file_name = 'created_charts\\bar_chart.png'

            ChartBar.set_title(ChartBar, title)
            ChartBar.set_y_label(ChartBar, y_label)
            ChartBar.set_labels(ChartBar, data_labels)
            ChartBar.set_fig_title(ChartBar, fig_title)

            ChartBar.create_bar_chart(ChartBar, data, output_file_name)

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
            data = [self.get_count_gender_f(), self.get_count_gender_m()]
        elif choice == 'sales':
            data_labels = "< 250", "250 - 499", "500 - 749", "750 - 999"
            title = "Sales Brackets of Staff"
            window_title = "Sales Brackets of Staff"
            data = [self.get_count_sales_group1(), self.get_count_sales_group2(),
                    self.get_count_sales_group3(), self.get_count_sales_group4()]
        else:
            print(Err.get_error_message(601))

        if title:
            attributes = {'title': title, 'data_labels': data_labels,
                          'window_title': window_title}
            chart.create_pie_chart(data, attributes)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
