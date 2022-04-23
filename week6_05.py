def group_by(func, iterable) -> dict:
    """
    The function will return a dictionary, in which:
    The keys are the values returned from the function passed as the first parameter.
    The value corresponding to a particular key is a list of all the organs for which the
    value appearing in the key is repeated.
    :param func:The function that is run on the iterable.
    :param iterable:All the element send to function.
    :return:A dictionary whose keys are the values returned from the function,
            And its values are the temp values corresponding to the key values.
    """

    return {func(key): list(filter(lambda item: func(item) == func(key), iterable)) for key in iterable}
    

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"])) 
