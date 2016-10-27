#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


def get_matches(players):
    """ This function matches objects in list.

    Args:
        players(list): Just a random list of strings.

    Returns:
        list: Tuples of args without repetitions.

    Examples:

    >>>get_matches(['Allison', 'Julia', 'Vera'])
    [('Allison', 'Julia'), ('Allison', 'Vera'), ('Julia', 'Vera')]
    """
    match = []
    for index0, item in enumerate(players):
        for index, pos in enumerate(players):
            if index > index0:
                match.append((item, pos))
    return match
