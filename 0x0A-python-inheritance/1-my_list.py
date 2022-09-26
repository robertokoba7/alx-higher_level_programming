#!/usr/bin/python3
class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        m_sorted = self.copy()
        m_sorted.sort()
        print(m_sorted)
