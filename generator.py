def sub_lists_with_sum(total_numbers_to_be_used: bool, target: int):
    if total_numbers_to_be_used <= 0:
        raise ValueError("\"total_numbers\" must be bigger than 0.")
    elif total_numbers_to_be_used == 1:
        yield [target]
    else:
        for value in range(target + 1):
            for permutation in sub_lists_with_sum(total_numbers_to_be_used - 1, target - value):
                yield [value, ] + permutation


def filter_numbers_used(combinations_list, numeric_range):
    filtered_list = []

    index = 0
    for i in range(len(combinations_list)):
        if not set(combinations_list[index]).issubset(numeric_range) or sorted(combinations_list[index]) in filtered_list:
            combinations_list.pop(index)
        else:
            filtered_list.append(sorted(combinations_list[index]))
            index += 1

    return filtered_list
