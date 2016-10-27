#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


import getpass
import authentication


def login(username, maxattempts=3):
    """ This function takes user input and allow or block access.

    Args:
        username(str): Arg to by typed by user.
        maxattempts(int, optional): Arg to be typed by user. Default: 3.

    Returns:
        str, bool: True if username and passowrd is correct. Otherwise return st
        ring with number of attempts left. If three incorrect attempts made retu
        rn False.

    Examples:

        >>> login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attemts left
        Please enter your password:
        Incorrect username or password. You have 2 attemts left
        Please enter your password:
        Incorrect username or password. You have 1 attemts left
        Please enter your password:
        Incorrect username or password. You have 0 attemts left
        False

        >>>login('violet', 1)
        Please enter your password:
        True
    """
    is_authenticated = False

    while maxattempts > 0 and is_authenticated is False:
        password = getpass.getpass('Please enter your password: ')
        if authentication.authenticate(username, password):
            is_authenticated = True
        else:
            maxattempts -= 1
            print ('Incorrect username or password. You have {0} attemts left'.
                   format(maxattempts))

    return is_authenticated
