from databases.pickler import Pickler
from error_dict import ErrorDict


class ErrorHandler(object):  # Claye

    @staticmethod
    def get_error_message(error_code, name=""):

        error_dict = ErrorDict.get_error_dict(name)

        try:
            return error_dict[error_code]
        except KeyError:
            return "Unknown Error"

    @staticmethod
    def send_data_to_pickler():
        to_pickle = ErrorDict.get_error_dict('')
        pickled = Pickler.pickle_list(to_pickle)
        return pickled
