from generator import sub_lists_with_sum, filter_numbers_used

from datetime import datetime
import pandas as pd
import pickle


def save_unfiltered_list(ls: list, name: str):
    print(f"[{datetime.now()}] Saving {name} pickle file")
    with open(f"{name}.pkl", "wb") as f:
        pickle.dump(ls, f, pickle.HIGHEST_PROTOCOL)


def load_unfiltered_list(name: str):
    print(f"[{datetime.now()}] Loading {name} pickle file")
    with open(f"{name}.pkl", "rb") as f:
        return pickle.load(f)


def get_combination_lists(target, numeric_range, save_unfiltered_lists):
    print(f"[{datetime.now()}] {total_numbers_to_be_used} numbers will be used to try to reach the sum of {target}.")
    print(f"[{datetime.now()}] The larger the \"target\" ({target}) is the longer this will take.")

    combinations_list = list(sub_lists_with_sum(total_numbers_to_be_used=total_numbers_to_be_used, target=target))
    if save_unfiltered_lists:
        save_unfiltered_list(combinations_list, f"target_{target}")
    combinations_list = filter_numbers_used(combinations_list=combinations_list, numeric_range=numeric_range)
    print(f"[{datetime.now()}] total permutations for target ({target}): {len(combinations_list)}\n")

    df_list = pd.DataFrame({"possible_set": combinations_list})
    df_list["total"] = [sum(x) for x in df_list["possible_set"]]

    df_list.to_csv(f"[{datetime.now()}] possible_combinations_{target}.csv", sep=",", header=True, index=False)

    return df_list


if __name__ == "__main__":
    save_unfiltered_lists = False
    total_numbers_to_be_used = 6
    numbers_to_be_used = range(0, 40)

    complete_df = pd.DataFrame()
    for t in range(60, 71)[::-1]:
        df = get_combination_lists(t, numbers_to_be_used, save_unfiltered_lists)
        complete_df = pd.concat([complete_df, df]).sort_values(by=["total"], ascending=False)
    complete_df.to_csv(f"possible_combinations.csv", sep=",", header=True, index=False)

    print("Done!")
