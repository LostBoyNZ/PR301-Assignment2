# Graham
import os
import sys


class Start:
    """
    Python Database Handler [Version 1.0]
    (c) 2018 Team Anaconda Ltd, all rights reserved.

    Authors: Claye Barry, Rochelle Wilson, Graham Parker

    """

    def __init__(self):

        print("Loading...")

        try:
            from errors import ErrorHandler as Err
        except NameError and ModuleNotFoundError and ImportError:
            print("Fatal Error - Errors.py not found.")
            sys.exit()

        try:
            from cmdline import CommandLine as Cmd
        except NameError and ModuleNotFoundError and ImportError:
            print(Err.get_error_message(404, "cmd"))
            sys.exit()

        os.system('cls')
        print(self.__doc__)

        user_args = []
        try:
            user_args = sys.argv[1:]
        except TypeError:
            pass

        Cmd().run_commandline(user_args)


i = Start()
