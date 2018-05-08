import sys

try:
    from charts.parent_chart import ParentChart
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - parent_chart.py not found.")
    sys.exit()

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


class ChartLine(ParentChart):
    def create_chart(self):
        age_list = self.get_data(self)[0]
        salary_list = self.get_data(self)[1]
        salary_list = [int(i) for i in salary_list]
        age_list = [int(i) for i in age_list]
        age_list, salary_list = zip(*sorted(zip(age_list, salary_list)))

        self.set_title(self, 'Salary Vs Age')
        self.set_y_label(self, 'Salary')
        self.set_x_label(self, 'Age of Staff')
        self.set_grid(self, True)

        list1 = age_list
        list2 = salary_list

        plt.plot(list1, list2)

        plt.title(self.get_title(self))
        plt.ylabel(self.get_y_label(self))
        plt.xlabel(self.get_x_label(self))
        plt.grid(self.get_grid(self))

        fig = plt.gcf()
        fig.canvas.set_window_title(self.get_title(self))
        plt.show()
        fig.savefig(self.get_output_file_name(self))
