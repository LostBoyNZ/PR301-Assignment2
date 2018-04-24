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
    def create_bar_chart(self, title, y_label, objects, data, fig_title):
        y_pos = np.arange(len(objects))
        plt.bar(y_pos, data, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel(y_label)
        plt.title(title)
        fig = plt.gcf()
        fig.canvas.set_window_title(fig_title)
        plt.show()
