import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Age': [21, 22, 20, 23],
    'Marks': [85, 90, 75, 95]
}

df = pd.DataFrame(data)

print(df)