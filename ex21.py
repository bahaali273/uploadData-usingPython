#Mapping using PY
import pandas as pd

data = pd.read_csv("emp.csv")
print(data)

gender_mapping={
    'M': 'Male',
    'F':'Female',
    'Male':'Male',
    'Female':'Female'
}

data["gender"]= data["gender"].map(gender_mapping)
print(data)

#to change in the exact file  we have to use this code
data.to_csv("emp2.csv")