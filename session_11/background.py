# In the beginning: no typehints
def repeat_list_as_string(my_list, number_of_repetitions):
    return ''.join(number_of_repetitions * my_list)


print(
    repeat_list_as_string(
        my_list=['a', 'b', 'c'],
        number_of_repetitions=2,
    ),
)

# Then: Docstring
def repeat_list_as_string_2(my_list, number_of_repetitions):
    """
    :param my_list: list
    :param number_of_repetitions: int
    :return: str
    """
    return ''.join(number_of_repetitions * my_list)


print(
    repeat_list_as_string_2(
        my_list=['a', 'b', 'c'],
        number_of_repetitions=2,
    ),
)
