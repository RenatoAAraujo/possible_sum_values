from temporary_files import save_file

from datetime import datetime
import numpy as np


def sub_lists_with_sum(total_numbers_to_be_used: bool, target: int):
    if total_numbers_to_be_used <= 0:
        raise ValueError("\"total_numbers\" must be bigger than 0.")
    elif total_numbers_to_be_used == 1:
        yield [target]
    else:
        for value in range(target + 1):
            for permutation in sub_lists_with_sum(total_numbers_to_be_used - 1, target - value):
                yield [value, ] + permutation


def filter_numbers_used(combinations_list, target, numeric_range, save_filtered_lists):
    print(f"[{datetime.now()}] Filtering list values out of range. List contains {len(combinations_list)} values")
    combinations_list = np.array(combinations_list)
    combinations_list = combinations_list[(combinations_list <= max(numeric_range)).all(axis=1)].tolist()
    if save_filtered_lists:
        save_file(combinations_list, f"target_{target}")
    print(f"[{datetime.now()}] After filtering list contains {len(combinations_list)} values")

    list_len = len(combinations_list)
    filtered_list = []

    index = 0
    for i in range(list_len):
        if i % 10000 == 0:
            print(f"[{datetime.now()}] {i}/{list_len}")
            if save_filtered_lists:
                save_file(filtered_list, f"temp_filtered_list_{target}")
                save_file(index, f"temp_index_{target}")

        if sorted(combinations_list[index]) in filtered_list:
            combinations_list.pop(index)
        else:
            filtered_list.append(sorted(combinations_list[index]))
            index += 1

    return filtered_list
