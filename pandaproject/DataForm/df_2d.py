# create first data frame using pandas

import pandas as pd


data = [['Audi', 'A5', 25000.490], ['BMW', 'X7', 32000.390], ['Mercedes', 'S200', 22000.750]] 

df = pd.DataFrame(data, columns=['Care Name', 'Models', 'Price'], dtype=float)

print(df)