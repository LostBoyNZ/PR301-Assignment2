import sys
import os
from databases.database_sqlite import CompanyDatabase

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Err.py not found.")
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()

try:
    from database_excel import DatabaseExcel as Dbexel
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "database_excel"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()

try:
    from data_fields import DataFields
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "data_fields"))
    sys.exit()
except Exception as e:
    print(Err.get_error_message(901, e))
    sys.exit()


class FileWriter(object):
    dict_root = {}

    def __init__(self):
        self.db = CompanyDatabase

    @staticmethod
    def get_input(text):
        return input(text)

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

    def write_file(self, dict_valid, my_controller):  # Claye
        u = self.get_input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            # Rochelle
            db = self.get_input("Do you want to save to a database or file?"
                                " D/F (default: F) >>> ")
            if db.upper() == "D":  # Rochelle
                self.write_to_database(self, dict_valid)  # Rochelle
            else:
                file_target = self.get_input("Please input filename to save"
                                             " to >>> ")
                if my_controller.check_path_exists(file_target):
                    u2 = self.get_input("File exists, do you want to append"
                                        " Y/N >>> ")
                    if u2.upper() == 'Y':
                        ids_already_in_file = self.remove_duplicates(
                            file_target)
                        self.commit_save(dict_valid, file_target,
                                         ids_already_in_file)
                    if u2.upper() == 'N':
                        self.write_file(self, dict_valid, my_controller)
                else:
                    self.commit_save(dict_valid, file_target)
        elif u.upper() == "N":
            print("Data Not saved")
        else:
            print(Err.get_error_message(102))

    def save_pickle_file(self, data_to_write):  # Claye, Graham
        u = self.get_input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            file_target = self.get_input("Please input the filename to save"
                                         " to >>> ")
            self.commit_pickle_save(file_target, data_to_write)
        elif u.upper() == "N":
            print("Data Not saved")

    @staticmethod
    def commit_pickle_save(file_target, data_to_write):  # Claye, Graham
        file = open(file_target, "wb")
        # data_to_write = str(data_to_write)
        file.write(data_to_write)
        file.close()

    # Claye and Graham
    @staticmethod
    def commit_save(dict_valid, file_target, ids_already_in_file=[]):
        dup_keys = 0
        rows_saved = 0
        rows = 0

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
            print(
                "All ID's already existed in the output file. Nothing added.")
        elif dup_keys > 0:
            print("{} of {} rows were duplicate keys and not inserted again".
                  format(dup_keys, rows))
            print("{} rows were added, and the file saved".format(rows_saved))

    # Rochelle
    def write_to_database(self, dict_valid):  # Rochelle
        db = CompanyDatabase()
        db.create_connection()

        data = []
        keys = []
        keys += dict_valid.keys()
        data += dict_valid.values()
        count = 0
        data_fields = DataFields.get_data_fields(DataFields)

        persons_attributes_list = []

        for item in data:
            if item['valid']:
                db_v = item['valid']
                db_id = keys[count]
                count += 1

                persons_attributes_list.append(db_id)

                # Ignore the ID field and the Valid field for now
                for row_name in data_fields[1:-1]:
                    try:
                        to_add = str(item[row_name]) + ","
                        persons_attributes_list.append(to_add)
                    except KeyError:
                        pass

                persons_attributes_list.append(db_v)
                db.insert_staff([persons_attributes_list])
                persons_attributes_list = []

        print(count, "persons added! Congratulations!")
        # Rochelle
        view_db = self.get_input(
            "Do you want to see data saved to database? Y/N >>> ")
        if view_db.upper() == "Y":
            db.get_staff()

        db.close()
