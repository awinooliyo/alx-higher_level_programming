#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    Args:
    - list_of_integers (list): The list of unsorted integers.

    Returns:
    - int or None: The peak value in the list or None if the list is empty.

    Note:
    - There may be more than one peak in the list.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if the peak is on the left side
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        # Check if the peak is on the right side
        else:
            low = mid + 1

    return list_of_integers[low]
