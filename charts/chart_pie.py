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

    def create_pie_chart(self, data, attributes):
        chart_data = ""
        title = attributes['title']
        data_labels = attributes['data_labels']
        window_title = attributes['window_title']

        sizes = data
        labels = data_labels

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title(title)
        fig = plt.gcf()
        fig.canvas.set_window_title(window_title)

        plt.show()
        fig.savefig('created_charts\\pie_chart.png')
