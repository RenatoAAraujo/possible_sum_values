def subsets_with_sum(numbers_to_be_used: bool, target: int):
    if numbers_to_be_used <= 0:
        raise ValueError("\"total_numbers\" must be bigger than 0.")
    elif numbers_to_be_used == 1:
        yield target,
    else:
        for value in range(target + 1):
            for permutation in subsets_with_sum(numbers_to_be_used - 1, target - value):
                yield (value,) + permutation


def filter_numbers_used(combinations_set, numeric_range):
    index = 0
    for i in range(len(combinations_set)):
        if not set(combinations_set[index]).issubset(numeric_range):
            combinations_set.pop(index)
        else:
            index += 1

    return combinations_set
