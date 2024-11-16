# create first data frame using pandas

import pandas as pd


data = [['Audi', 'A5', 25590.49], ['BMW', 'X7', 32355.99], ['Mercedes', 'S200', 22000.75]] 

df = pd.DataFrame(data, columns=['Care Name', 'Models', 'Price'], dtype=float)

print(df)