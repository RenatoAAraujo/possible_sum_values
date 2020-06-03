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
    print(f"[{datetime.now()}] [{target}] Filtering list values out of range. List contains {len(combinations_list)} values")
    combinations_list = np.array(combinations_list)
    combinations_list = combinations_list[(combinations_list <= max(numeric_range)).all(axis=1)]
    combinations_list.sort(axis=1)
    if save_filtered_lists:
        save_file(combinations_list, f"target_{target}")
    print(f"[{datetime.now()}] [{target}] After filtering list contains {len(combinations_list)} values")

    filtered_list = np.unique(combinations_list, axis=0)

    return filtered_list.tolist()
