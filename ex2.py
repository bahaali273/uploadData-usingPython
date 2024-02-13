import pandas as pd

data = pd.read_excel("Canada.xlsx", sheet_name="Canada by Citizenship", skiprows=20)
print(data.head(20))

