# Rochelle
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

try:
    import numpy as np
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "numpy"))
    sys.exit()


class ChartBar(ParentChart):
    def create_chart(self):
        y_pos = np.arange(len(self.get_fig_labels(self)))
        plt.bar(y_pos, self.get_data(self), align='center', alpha=0.5)
        plt.xticks(y_pos, self.get_fig_labels(self))

        plt.ylabel(self.get_y_label(self))
        plt.title(self.get_title(self))

        fig = plt.gcf()
        fig.canvas.set_window_title(self.get_title(self))
        plt.show()
        fig.savefig(self.get_output_file_name(self))
