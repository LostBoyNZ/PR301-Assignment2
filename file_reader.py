import os.path
import sys

from openpyxl import load_workbook

from data_processor import DataProcessor
from databases.database_sqlite import CompanyDatabase
from log_file_handler import LogFileHandler

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Err.py not found.")
    sys.exit()

try:
    from database_excel import DatabaseExcel as Dbexel
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "database_excel"))
    sys.exit()


class FileReader(object):  # Claye

    dict_root = {}

    def __init__(self):
        self.db = CompanyDatabase

    def call_file(self, switch, separator):
        file_name = input("Please enter the filename to read data from >>> ")
        split_filename = file_name.split(".")
        file_extension = split_filename[-1]
        if file_extension == "xls" or file_extension == "xlsx":
            try:
                wb = load_workbook(file_name)
            except FileNotFoundError:
                print(Err.get_error_message(201))
                self.call_file(switch)
            except OSError:
                print(Err.get_error_message(103))
                self.call_file(switch)

            i = Dbexel()
            data_to_save = i.create_connection(wb, switch)
            self.write_file(data_to_save)
        elif file_extension == "txt" or file_extension == "csv":
            try:
                self.split_file(file_name, switch, separator)
            except FileNotFoundError:
                print(Err.get_error_message(201))
                self.call_file(switch)
            except OSError:
                print(Err.get_error_message(103))
                self.call_file(switch)
        else:
            print(Err.get_error_message(204))

    # Claye, Works with CSV and TXT docs
    def split_file(self, file_name, switch, separator=","):
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        else:
            # Repeat for each line in the text file
            f = FileReader()
            dup_keys = 0
            keep_going = True

            for line in file:
                # Split file into fields using ","
                fields = line.split(separator)
                checked_id = DataProcessor.validate_key(fields[0])
                if checked_id in f.dict_root:
                    dup_keys += 1
                    fields[6] = fields[6].rstrip()
                    data_to_log = "Duplicate Key" + str(fields[0:])
                    LogFileHandler.append_file('log.txt', data_to_log)
                else:
                    try:
                        f.dict_root.update({checked_id: {'gender': fields[1],
                                                       'age': fields[2],
                                                       'sales': fields[3],
                                                       'bmi': fields[4],
                                                       'salary': fields[5],
                                                       'birthday': fields[6]
                                         .rstrip(),
                                                       'valid': '0'}})
                    except IndexError:
                        print(Err.get_error_message(211))
                        keep_going = False
            # Close the file to free up resources (good practice)
            file.close()
            if keep_going:
                valid_dict = DataProcessor.send_to_validate(f.dict_root,
                                                            switch, dup_keys)
                self.write_file(valid_dict)

    @staticmethod
    def remove_duplicates(file_name):   # Graham
        ids_already_in_file = []

        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        else:
            for line in file:
                fields = line.split(',')
                if fields[0] != "\n":
                    ids_already_in_file.append(fields[0])

            file.close()

        return ids_already_in_file

    def write_file(self, dict_valid):  # Claye
        u = input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            # Rochelle
            db = input("Do you want to save to a database ot file? D/F >>> ")
            if db.upper() == "D":  # Rochelle
                self.write_to_database(dict_valid)  # Rochelle
            elif db.upper() == "F":
                file_target = input("Please input filename to save to >>> ")
                if self.check_path_exists(file_target):
                    u2 = input("File exists, do you want to append Y/N >>> ")
                    if u2.upper() == 'Y':
                        ids_already_in_file = self.remove_duplicates(file_target)
                        self.commit_save(dict_valid, file_target, ids_already_in_file)
                    if u2.upper() == 'N':
                        self.write_file(dict_valid)
                else:
                    self.commit_save(dict_valid, file_target)
            else:
                print(Err.get_error_message(102))
                self.write_file(dict_valid)
        elif u.upper() == "N":
            print("Data Not saved")
        else:
            print(Err.get_error_message(102))
            self.write_file(dict_valid)

    def save_pickle_file(self, data_to_write):  # Claye, Graham
        u = input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            file_target = input("Please input the filename to save to >>> ")
            self.commit_pickle_save(file_target, data_to_write)
        elif u.upper() == "N":
            print("Data Not saved")

    def load_pickle_file(self):  # Claye, Graham
        file_target = input("Please input the filename to load from >>> ")
        # self.commit_pickle_save(file_target, data_to_write)
        try:
            file = open(file_target, "rb")
        except FileNotFoundError:
            print(Err.get_error_message(201))
        except OSError:
            print(Err.get_error_message(103))

        with open(file_target) as file:
            lines = file.readlines()

        print(lines)
        return lines

    @staticmethod
    def commit_pickle_save(file_target, data_to_write):  # Claye, Graham
        file = open(file_target, "wb")
        data_to_write = str(data_to_write)
        file.write(data_to_write + "\n")
        file.close()

    def commit_save(self, dict_valid, file_target, ids_already_in_file=[]):  # Claye and Graham
        dup_keys = 0
        rows_saved = 0
        rows = 0

        try:
            z = open(file_target, "a")
            for key in dict_valid:
                if key not in ids_already_in_file:
                    z.write("\n")
                    z.write(key + ",")
                    for value in dict_valid[key]:
                        h = str(dict_valid[key][value] + ",")
                        z.write(value + ' ' + h)

                    rows_saved += 1
                    rows += 1
                else:
                    dup_keys += 1
                    rows += 1
            z.write("\n")
            z.close()
            if dup_keys == 0:
                print("File saved, {} rows added".format(rows_saved))
            elif dup_keys == rows:
                print("All ID's already existed in the output file. Nothing added.")
            elif dup_keys > 0:
                print("{} of {} rows were duplicate keys and not inserted again".format(dup_keys, rows))
                print("{} rows were added, and the file saved".format(rows_saved))
        except OSError:
            print(Err.get_error_message(103))
            self.write_file(dict_valid)

    @staticmethod
    def check_path_exists(path):  # Claye
        result = False
        try:
            if os.path.exists("{}".format(path)):
                result = True
                return result
            else:
                return result
        except OSError:
            print(Err.get_error_message(103))

    # Rochelle
    def write_to_database(self, dict_valid):  # Rochelle

        db = CompanyDatabase()
        db.create_connection()

        data = []
        keys = []
        keys += dict_valid.keys()
        data += dict_valid.values()
        count = 0

        for item in data:
            if item['valid'] == '1':
                db_v = item['valid']
                db_id = keys[count]
                count += 1
                if item['gender']:
                    db_g = item['gender'] + ","
                if item['age']:
                    db_a = item['age'] + ","
                if item['sales']:
                    db_sale = item['sales'] + ","
                if item['bmi']:
                    db_bm = item['bmi'] + ","
                if item['salary']:
                    db_sala = item['salary'] + ","
                if item['birthday']:
                    db_bi = item['birthday'] + ","

                db.insert_staff([(db_id, db_g, db_a, db_sale, db_bm,
                                  db_sala, db_bi, db_v)])

        print(count, "persons added! Congratulations!")
        # Rochelle
        view_db = input("Do you want to see data saved to database? Y/N >>> ")
        if view_db.upper() == "Y":
            db.get_staff()

        db.close()
