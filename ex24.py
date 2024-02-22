#Box Plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("lr3.csv")

sns.boxplot(x='Attendance', y='GPA', data=data)
plt.show()