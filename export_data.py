from generator import sub_lists_with_sum, filter_numbers_used

from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from datetime import datetime
from multiprocessing import cpu_count
import pandas as pd


def get_combination_lists(target, numeric_range, save_filtered_lists):
    print(f"[{datetime.now()}] {total_numbers_to_be_used} numbers will be used to try to reach the sum of {target}.")
    print(f"[{datetime.now()}] The larger the \"target\" ({target}) is the longer this will take.")

    combinations_list = list(sub_lists_with_sum(total_numbers_to_be_used, target))
    combinations_list = filter_numbers_used(combinations_list, target, numeric_range, save_filtered_lists)
    print(f"[{datetime.now()}] total permutations for target ({target}): {len(combinations_list)}\n")

    df_list = pd.DataFrame({"possible_set": combinations_list})
    df_list["total"] = [sum(x) for x in df_list["possible_set"]]

    df_list.to_csv(f"possible_combinations_{target}.csv", sep=",", header=True, index=False)

    return df_list


if __name__ == "__main__":
    make_temporary_files = False
    total_numbers_to_be_used = 6
    numbers_to_be_used = range(0, 5)

    if cpu_count() > 3:
        executor = ThreadPoolExecutor(cpu_count() - 3)
    else:
        executor = ThreadPoolExecutor(cpu_count() - 1)
    complete_df_list = list()
    complete_df = pd.DataFrame()
    
    for t in range(0, 10)[::-1]:
        complete_df_list.append(executor.submit(get_combination_lists, t, numbers_to_be_used, make_temporary_files))
    for i in as_completed(complete_df_list):
        complete_df = pd.concat([complete_df, i.result()]).sort_values(by=["total"], ascending=False)
    
    complete_df.to_csv(f"possible_combinations.csv", sep=",", header=True, index=False)

    print("Done!")
