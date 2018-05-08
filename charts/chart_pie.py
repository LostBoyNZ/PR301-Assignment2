# Graham
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


class ChartPie(ParentChart):  # Graham
    def create_chart(self):
        sizes = self.get_data(self)
        labels = self.get_fig_labels(self)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title(self.get_fig_title(self))
        fig = plt.gcf()
        fig.canvas.set_window_title(self.get_title(self))

        plt.show()
        fig.savefig(self.get_output_file_name(self))
