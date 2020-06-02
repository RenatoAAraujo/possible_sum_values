from generator import sub_lists_with_sum, filter_numbers_used

from datetime import datetime
import pandas as pd


def get_combination_lists(target, save_filtered_lists):
    print(f"[{datetime.now()}] {total_numbers_to_be_used} numbers will be used to try to reach the sum of {target}.")
    print(f"[{datetime.now()}] The larger the \"target\" ({target}) is the longer this will take.")

    combinations_list = list(sub_lists_with_sum(total_numbers_to_be_used=total_numbers_to_be_used, target=target))
    combinations_list = filter_numbers_used(combinations_list=combinations_list, target=target, save_filtered_lists=save_filtered_lists)
    print(f"[{datetime.now()}] total permutations for target ({target}): {len(combinations_list)}\n")

    df_list = pd.DataFrame({"possible_set": combinations_list})
    df_list["total"] = [sum(x) for x in df_list["possible_set"]]

    df_list.to_csv(f"[{datetime.now()}] possible_combinations_{target}.csv", sep=",", header=True, index=False)

    return df_list


if __name__ == "__main__":
    save_filtered_lists = False
    total_numbers_to_be_used = 6
    numbers_to_be_used = range(0, 40)

    complete_df = pd.DataFrame()
    for t in range(60, 71)[::-1]:
        df = get_combination_lists(t, save_filtered_lists)
        complete_df = pd.concat([complete_df, df]).sort_values(by=["total"], ascending=False)
    complete_df.to_csv(f"possible_combinations.csv", sep=",", header=True, index=False)

    print("Done!")
