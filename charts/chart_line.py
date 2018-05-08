import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    import matplotlib.pyplot as plt
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "matplotlib.pyplot"))
    sys.exit()


class ChartLine(object):
    salary_list = []
    age_list = []
    title = ""
    y_label = ""
    x_label = ""
    grid = False

    def set_salary_list(self, new_data):
        self.salary_list = new_data

    def set_age_list(self, new_data):
        self.age_list = new_data

    def set_title(self, new_data):
        self.title = new_data

    def set_y_label(self, new_data):
        self.y_label = new_data

    def set_x_label(self, new_data):
        self.x_label = new_data

    def set_grid(self, new_data):
        self.grid = new_data

    def get_salary_list(self):
        return self.salary_list

    def get_age_list(self):
        return self.age_list

    def get_title(self):
        return self.title

    def get_y_label(self):
        return self.y_label

    def get_x_label(self):
        return self.x_label

    def get_grid(self):
        return self.grid

    def create_line_grid(self, data1, data2, output_file_name):
        age_list = data1
        salary_list = data2
        salary_list = [int(i) for i in salary_list]
        age_list = [int(i) for i in age_list]
        age_list, salary_list = zip(*sorted(zip(age_list, salary_list)))

        self.set_salary_list(self, salary_list)
        self.set_age_list(self, age_list)

        self.set_title(self, 'Salary Vs Age')
        self.set_y_label(self, 'Salary')
        self.set_x_label(self, 'Age of Staff')
        self.set_grid(self, True)

        list1 = self.get_age_list(self)
        list2 = self.get_salary_list(self)

        plt.plot(list1, list2)

        plt.title(self.get_title(self))
        plt.ylabel(self.get_y_label(self))
        plt.xlabel(self.get_x_label(self))
        plt.grid(self.get_grid(self))

        fig = plt.gcf()
        fig.canvas.set_window_title(self.get_title(self))
        plt.show()
        fig.savefig('created_charts\\line_chart.png')
