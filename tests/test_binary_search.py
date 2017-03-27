from lib.binary_search import binary_search, recursive_binary_search


def test_binary_search():
    """ Testing binary_search

    >>> binary_search([1,3,5,7,9,11,13,15,17,19], 4) is None
    True

    >>> binary_search([1,3,5,7,9,11,13,15,17,19], 3)
    1

    >>> binary_search([1,3,5,7,9,11,13,15,17,19], 7)
    3

    >>> binary_search([1,3,5,7,9,11,13,15,17,19], 1)
    0

    >>> binary_search([1,3,5,7,9,11,13,15,17,19], 19)
    9
    """

def test_recursive_binary_search():
    """ Testing binary_search

        >>> recursive_binary_search([1,3,5,7,9,11,13,15,17,19], 4) is None
        True

        >>> recursive_binary_search([1,3,5,7,9,11,13,15,17,19], 3)
        1

        >>> recursive_binary_search([1,3,5,7,9,11,13,15,17,19], 7)
        3

        >>> recursive_binary_search([1,3,5,7,9,11,13,15,17,19], 1)
        0

        >>> recursive_binary_search([1,3,5,7,9,11,13,15,17,19], 19)
        9
        """