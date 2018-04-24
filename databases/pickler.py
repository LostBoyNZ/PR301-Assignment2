# Rochelle
from io import BytesIO
from pickle import Unpickler
from pickle import dumps


class Pickler(object):
    @staticmethod
    def pickle_data(data):
        p = []  # pickled_list
        for value in data:
            pickled = dumps(value)
            p.append(pickled)
        return p

    @staticmethod  # Claye, Pickles a dict to keep data in key:value pairs
    def pickle_list(data):
        pickled = dumps(data)
        return pickled

    @staticmethod
    def unpickle_data(data):
        un_p = []  # un-pickled list
        for value in data:
            file = BytesIO(value)
            un_pickled = Unpickler(file).load()
            un_p.append(un_pickled)
        return un_p
