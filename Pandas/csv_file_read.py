import pandas as pd

df = pd.read_csv('data-store.csv', skiprows=1)
print(df)