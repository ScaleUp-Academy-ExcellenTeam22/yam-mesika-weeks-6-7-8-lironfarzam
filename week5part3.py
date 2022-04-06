def all_perfect_numbers():
    """
    Generator function that ran to infinity
    Returns the next perfect number in each reading.
    Perfect number: one whose sum of divisors is equal to the number itself
    :return:Perfect number one at a time
    """
    index = int(2)
    while True:
        if sum(x for x in range(1, index) if not index % x) == index:
            yield index
        index = index + 1


if __name__ == '__main__':

    all_perfect_numbers_generator = all_perfect_numbers()

    print(next(all_perfect_numbers_generator))
    print(next(all_perfect_numbers_generator))
    print(next(all_perfect_numbers_generator))
    print(next(all_perfect_numbers_generator))

    # # Warning!!!
    # # After the 4 call the computer get really hot...
    # print(next(all_perfect_numbers_generator))
