""" This class is for the history cache"""
# import the namespaces


class Calculations:
    """ This is the static Calculator class"""
    # history is a static property
    history = []

    @staticmethod
    def clear_history():
        """ clears the history cache"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """ returns how many calculations are in history"""
        return len(Calculations.history)

    @staticmethod
    def add_to_history(calculation):
        """ adds the result to history cache"""
        return Calculations.history.append(calculation)

    @staticmethod
    def get_first_result():
        """ 0 gets the first item added to the history cache"""
        return Calculations.history[0]

    @staticmethod
    def get_history_result():
        """ -1 gets the most recent item added to the history cache"""
        return Calculations.history[-1]

    @staticmethod
    def get_specified_result(num):
        """ Gets the indexed item from history cache """
        return Calculations.history[num]
