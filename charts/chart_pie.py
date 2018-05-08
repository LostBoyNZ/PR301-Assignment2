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
    import matplotlib.pyplot as plt
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "matplotlib.pyplot"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()


class ChartPie(object):  # Graham
    data_labels = ""
    data = []
    title = ""
    fig_title = ""
    y_label = ""
    x_label = ""
    grid = False
    output_file_name = ""

    def set_labels(self, new_data):
        self.data_labels = new_data

    def set_data(self, new_data):
        self.data = new_data

    def set_title(self, new_data):
        self.title = new_data

    def set_fig_title(self, new_data):
        self.fig_title = new_data

    def set_y_label(self, new_data):
        self.y_label = new_data

    def set_x_label(self, new_data):
        self.x_label = new_data

    def set_grid(self, new_data):
        self.grid = new_data

    def set_output_file_name(self, new_data):
        self.output_file_name = new_data

    def get_labels(self):
        return self.data_labels

    def get_data(self):
        return self.data

    def get_title(self):
        return self.title

    def get_fig_title(self):
        return self.fig_title

    def get_y_label(self):
        return self.y_label

    def get_x_label(self):
        return self.x_label

    def get_grid(self):
        return self.grid

    def get_output_file_name(self):
        return self.output_file_name

    def create_pie_chart(self):
        sizes = self.get_data(self)
        labels = self.get_labels(self)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title(self.get_fig_title(self))
        fig = plt.gcf()
        fig.canvas.set_window_title(self.get_title(self))

        plt.show()
        fig.savefig(self.get_output_file_name(self))
