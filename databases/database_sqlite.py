# Rochelle
import sqlite3
from sqlite3 import Error

from databases.pickler import Pickler


class CompanyDatabase(object):
    """Class for initializing a new or connect to an existing database."""
    _connection = None
    _cursor = None

    def __init__(self, database="company.db"):
        """Initialize new field to be part of a database."""
        self.database = database

    def create_connection(self):
        """ Create a database connection to a database that resides
            in the memory
        """
        try:
            self._connection = sqlite3.connect(self.database)
            self._cursor = self._connection.cursor()
            self.drop_staff_table()
            self.create_staff_table()
        except Error as e:
            print("An error occurred:", e)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connecting to database")

    def create_staff_table(self):
        sql_command = """
        CREATE TABLE Staff (
        emp_id TEXT PRIMARY KEY,
        gender VARCHAR(1),
        age INT,
        sales INT,
        bmi VARCHAR(12),
        salary INT,
        birthday DATE,
        valid INT);"""
        self._cursor.execute(sql_command)

    def insert_staff(self, staff):
        """insert staff into the table"""
        count = 1
        try:
            for person in staff:
                p = Pickler.pickle_data(person)
                self._cursor.execute("""INSERT INTO Staff (emp_id, gender, 
                age, sales, bmi, salary, birthday, valid)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (
                p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
                print(count, "Person added")
                count += 1
                self.commit()
        except sqlite3.IntegrityError:
            print('That record already exists')
        except IndexError:
            print('List index out of range')
        except sqlite3.OperationalError:
            print("Oops! This was an operational error. Try again...")
        except TypeError:
            print("Type Error")
        except ValueError:
            print("Value error")
        except IOError:
            print("IO error")
        finally:
            print("Finished inserting into database")

    def get_staff(self):
        """get all staff from the table"""
        try:
            self._cursor.execute("SELECT * FROM Staff")
            rows = self._cursor.fetchall()
            for row in rows:
                un_pickled = Pickler.unpickle_data(row)
                print(un_pickled)
        except Error as e:
            print("An error occurred:", e)

    def drop_staff_table(self):
        """Drop table if exists"""
        self._cursor.execute("""DROP TABLE IF EXISTS Staff;""")

    def commit(self):
        """Commit the database."""
        self._connection.commit()

    def close(self):
        """Close the database."""
        self._connection.close()
