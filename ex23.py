# Inferential Analysis

import pandas as pd
data = pd.read_csv("house.csv")

from scipy import stats

group1 = data[data["bdrms"] == 2]["price"]
group2 = data[data["bdrms"] == 3]["price"]


_, p_value = stats.ttest_ind(group1, group2)
print(p_value)

if p_value < 0.1:
    print("significant effect")
else:
    print("no significant effect")