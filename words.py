def print_upper_words(words):
    """ For each word, print on a new line and uppercase.
        >>> print_upper_words(['Lorem', 'ipsum', 'dolor', 'sit', 'amet'])
        LOREM
        IPSUM
        DOLOR
        SIT
        AMET
    """

    for word in words:
        print(word.upper())


def print_upper_words_start_e(words):
    """ For every word with e/E, print on new line and uppercase.
        >>> print_upper_words_start_e(['every', 'costco', 'Español'])
        EVERY
        ESPAÑOL
    """

    for word in words:
        if word[0] == ('E') or word[0] == ('e'):
            print(word.upper())


def print_upper_words_spec(words, must_start_with):
    """ Print words including spec char, uppercased, on new line 
    >>> print_upper_words_spec(['every', 'costco', 'Español', 'money'], ['c', 'E']
    """

    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())
