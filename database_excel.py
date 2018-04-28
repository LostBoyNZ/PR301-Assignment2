# Graham
import sys
from datetime import datetime

from openpyxl import load_workbook

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()
except Exception as e:
    print("Exception: {}".format(e))

try:
    from data_processor import DataProcessor as dp
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "data_processor"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))

try:
    from log_file_handler import LogFileHandler as Lfh
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "log_file_handler"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))


class DatabaseExcel(object):  # Graham

    row_names = ['emp_id', 'gender', 'age', 'sales',
                 'bmi', 'salary', 'birthday', 'valid']

    @staticmethod
    def get_input(text):
        return input(text)

    def choose_sheet(self, wb):
        sheet_names = wb.sheetnames
        # default to the first sheet
        sheet = wb.worksheets[0]

        if len(sheet_names) > 1:
            print("Sheets:\n")
            i = 1
            for sheet in sheet_names:
                print(str(i) + ") " + sheet)
                i += 1

            while True:
                sheet_number = self.get_input("\nEnter the sheet number to read >>> ")
                try:
                    sheet_number -= 1
                    sheet = wb.worksheets[int(sheet_number)]
                    break
                except IndexError or KeyError or ValueError:
                    print(Err.get_error_message(102, sheet_number))
                except TypeError:
                    print(Err.get_error_message(106, "numbers"))

        return sheet

    def choose_file(self):
        while True:
            file_name = self.get_input("\nPlease enter the excel file to read >>> ")
            wb = None

            try:
                wb = load_workbook(file_name)
                break
            except FileNotFoundError:
                print(Err.get_error_message(201))

        return wb

    def create_connection(self, wb, switch):
        sheet = self.choose_sheet(self, wb)

        target_column = 2
        target_row = 1

        max_column = sheet.max_column
        max_row = sheet.max_row

        data_row = []
        row_dict = {}
        keys = []
        data_to_process = {}

        i = 0
        dup_keys = 0
        for row in self.row_names:
            row_dict[self.row_names[i]]: ''
            i = i + 1

        for row in range(0, max_row):

            # Get the first value from the row to set as the key
            output = sheet.cell(row=target_row, column=1).value
            key = dp.validate_key(str(output))

            # Check if it's a duplicate key
            if key in keys:
                dup_keys += 1
                data_to_log = "Duplicate Key" + str(key)
                Lfh.append_file('log.txt', data_to_log)

            # Add that key to the list of all keys
            keys.append(key)
            data_to_process[key] = {}

            col_num = 0
            for column in range(0, max_column):
                output = sheet.cell(row=target_row, column=target_column).value
                data_row.append(str(output))

                row_dict[self.row_names[col_num]] = data_row[col_num]
                target_column = target_column + 1
                col_num = col_num + 1

            # Skip the ID and Valid rows
            for row in self.row_names[1:-1]:
                data_to_process[key][row] = row_dict[row]

            data_to_process[key]['valid'] = "0"

            data_row = []
            target_column = 1
            target_row = target_row + 1

        # Send the data to be processed
        dict_valid = dp.send_to_validate(data_to_process, switch, dup_keys)

        return dict_valid
