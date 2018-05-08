# Rochelle
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

try:
    import numpy as np
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "numpy"))
    sys.exit()


class ChartBar(object):
    data_labels = []
    title = ""
    fig_title = ""
    y_label = ""
    x_label = ""
    grid = False
    words = []

    def set_labels(self, new_data):
        self.data_labels = new_data

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

    def get_labels(self):
        return self.data_labels

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

    def create_bar_chart(self, data, output_file_name):
        y_pos = np.arange(len(self.get_labels(self)))
        plt.bar(y_pos, data, align='center', alpha=0.5)
        plt.xticks(y_pos, self.get_labels(self))

        plt.ylabel(self.get_y_label(self))
        plt.title(self.get_title(self))

        fig = plt.gcf()
        fig.canvas.set_window_title(self.get_title(self))
        plt.show()
        fig.savefig(output_file_name)
