from typing import List


def repeat_list_as_string_3(my_list: List, number_of_repetitions: int) -> str:
    return ''.join(number_of_repetitions * my_list)


print(
    repeat_list_as_string_3(
        my_list=['a', 'b', 'c'],
        number_of_repetitions=2.2,
    ),
)