from datetime import datetime, timedelta

FIRST_ROW_OF_KEYBOARD = set("qwertyuiop")
SECOND_ROW_OF_KEYBOARD = set("asdfghjkl")
THIRD_ROW_OF_KEYBOARD = set("zxcvbnm")


def average_runtime(data_array, word_to_search: str, times_to_run: int = 1000) -> timedelta:
    """
    A function will get an array of strings that measures how long it took on average to find the the_word in the array.
    :param data_array: array of strings.
    :param word_to_search: string to fine in the array.
    :param times_to_run: How many times search for the the_word.
    :return: The average time the search took.
    """

    start_time = datetime.now()
    for index in range(0, times_to_run):
        temp_bool_for_result_not_in_use = word_to_search in data_array
    end_time = datetime.now()

    return (end_time - start_time) / times_to_run


def possible_to_write_by_one_line(the_word: str) -> bool:
    """
    Get string and return if is possible to write the string whit only one line of the keyboard.
    :param the_word: the string
    :return: True or False
    """
    set_word = set(the_word)
    return set_word <= FIRST_ROW_OF_KEYBOARD or set_word <= SECOND_ROW_OF_KEYBOARD or set_word <= THIRD_ROW_OF_KEYBOARD


def find_special_state(list_of_stats: [str]) -> []:
    """
    function get list of state and return list of stats is possible to write them whit only one line of the keyboard.
    :param list_of_stats: list of states
    :return: list of all the special states
    """
    return list(filter(possible_to_write_by_one_line, list_of_stats))


if __name__ == '__main__':

    # opening the file in read mode
    file_of_all_words = open("words.txt", "r")
    data = file_of_all_words.read()
    words_list = data.split("\n")
    words_set = set(words_list)

    word = "Hii"
    times = 1000

    print("On list average time to search: ", average_runtime(words_list, word_to_search=word, times_to_run=times))
    print("On set average time to search: ", average_runtime(words_list, word_to_search=word, times_to_run=times))

    file_of_all_words.close()

    file_of_all_states = open("states.txt", "r")
    data = file_of_all_states.read()
    states_list = data.split("\n")

    print("\n")
    print("List of all special states:")
    print(find_special_state(states_list))

    file_of_all_states.close()
