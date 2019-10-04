__author__ = 'Fabian Nemazi'
__email__ = 'fabinema@nmbu.no'


def bubble_sort(in_data):
    s_data = list(in_data)
    for j in reversed(range(len(s_data))):
        for k in range(j):
            if s_data[k + 1] < s_data[k]:
                s_data[k], s_data[k + 1] = s_data[k + 1], s_data[k]
    return s_data


def test_empty():
    assert bubble_sort(()) == [], 'Test to see if bubble_sort works on' \
                                  'empty lists'
    assert bubble_sort([]) == [], 'Test to see if bubble_sort works on' \
                                  'empty lists'


def test_single():
    assert bubble_sort([1]) == [1], 'Testing bubble_sort for one-element' \
                                    'lists.'


def test_sorted_is_not_original():
    """Test that the sorting function returns a new object."""
    first_list = [1, 9, 17, 4, 7, 8]
    new_list = bubble_sort(first_list)
    assert new_list != first_list, 'Testing bubble_sort to see if sorting' \
                                   'function returns new object.'


def test_original_unchanged():
    """Test that sorting leaves the original data unchanged."""
    first_list = [1, 9, 17, 4, 7, 8]
    bubble_sort(first_list)
    assert first_list == [1, 9, 17, 4, 7, 8], 'Test that sorting leaves' \
                                              'original data unchanged'


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    assert bubble_sort([1, 2, 3, 4, 5, 10, 17]) == [1, 2, 3, 4, 5, 10, 17], \
        'Test that sorting works on sorted data'


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10], \
        'Test sorting for reversed data'


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([1, 8, 3, 4, 5, 6, 8, 2, 3]) == [1, 2, 3, 3, 4, 5, 6, 8,
                                                        8], \
        'Test sorting function to see if it' \
        'works for identical element in list'


def test_for_negative_elements():
    test_list = [4, 3, 7, 1, -4, -2, 0]
    assert bubble_sort(test_list) == [-4, -2, 0, 1, 3, 4, 7], 'Test for negative' \ 'numbers'


def test_for_letters():
    try:
        bubble_sort(['n', 'o', 'r', 'w', 'a', 'y'])
    except ValueError:
        print('You cannot use strings')



