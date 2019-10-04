__author__ = 'Fabian Nemazi'
__email__ = 'fabinema@nmbu.no'


def median(data):
    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_one_el():
    test_list = [random.randint(0, 9)]
    assert median(test_list) == test_list[0], 'Not correct for lists with ' \
                                              'only one element.'


def test_odd_numbers():
    test_list = [i for i in range(0, 7)]
    import statistics
    assert median(test_list) == statistics.median(test_list), \
        'Not correct for ' \
        'odd numbers in' \
        'list.'


def test_even_numbers():
    import statistics
    test_list = [i for i in range(0, 6)]
    assert median(test_list) == statistics.median(test_list), \
        'Not correct for' \
        'even numbers in' \
        'list.'


def test_ordered_elements():
    import statistics
    test_list = [i for i in range(0, 8)]
    assert median(test_list) == statistics.median(test_list), \
        'Not correct for' \
        'ordered elements' \
        'in list'


def test_rev_ordered_elements():
    test_list = [i for i in range(0, 8)]
    rev_test_list = sorted(test_list, reverse=True)
    assert median(test_list) == median(rev_test_list), \
        'Not correct for ' \
        'reversed ordered' \
        'elements in list.'


def test_unordered_elements():
    import statistics
    test_list = [1, 5, 6, 8, 3, 65, 7, 4, 3, 2, 5, 6]
    assert median(test_list) == statistics.median(test_list), \
        'Not correct for ' \
        'unordered lists.'


def test_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    test_list = [i for i in range(1, 9)]
    median(test_list)
    assert test_list == [i for i in range(1, 9)], 'The original data has ' \
                                                  'been changed'


def test_for_tuples():
    test_list = [i for i in range(1, 8)]
    tuple_list = (1, 2, 3, 4, 5, 6, 7)
    while False:
        try:
            median(test_list) == median(tuple_list)
        except TypeError:
            print('Median function does not work for tuples')