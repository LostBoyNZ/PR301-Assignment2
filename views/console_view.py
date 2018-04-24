class ConsoleView:
    def __init__(self):
        pass

    @staticmethod
    def show_output(message):
        print(message)

    @staticmethod
    def get_input(prompt):
        user_command = input(prompt)

        return user_command
