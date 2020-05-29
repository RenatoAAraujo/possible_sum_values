from generator import subsets_with_sum

import pandas as pd

if __name__ == "__main__":
    combinations_set = subsets_with_sum(
            numbers_set=list(range(1, 40)),
            with_replacement=True,
            target=70
        )

    df_set = pd.DataFrame({"possible_set": combinations_set})
    df_set.to_csv("possible_combinations.csv", sep=",", header=True, index=False)
    print("Done!")
