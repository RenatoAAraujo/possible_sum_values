from generator import subsets_with_sum, filter_numbers_used

import pandas as pd


def get_combination_sets(target):
    print(f"{numbers_to_be_used} numbers will be used to try to reach the sum of {target}.\n")
    print(f"The larger the \"target\" ({target}) is the longer this will take.")

    combinations_set = list(subsets_with_sum(numbers_to_be_used=numbers_to_be_used, target=target))
    combinations_set = filter_numbers_used(combinations_set=combinations_set, numeric_range=range(0, 40))
    print(f"total permutations for target ({target}): {len(combinations_set)}")

    df_set = pd.DataFrame({"possible_set": combinations_set})
    df_set["total"] = [sum(x) for x in df_set["possible_set"]]

    df_set.to_csv(f"possible_combinations_{target}.csv", sep=",", header=True, index=False)

    return df_set


if __name__ == "__main__":
    numbers_to_be_used = 6

    complete_df = pd.DataFrame()
    for t in range(60, 71):
        df = get_combination_sets(t)
        complete_df = pd.concat([complete_df, df])
    complete_df.to_csv(f"possible_combinations.csv", sep=",", header=True, index=False)

    print("Done!")
