# create dataframe using dictionary

import pandas as pd

# create data using dictionary

data = {'Name': ['Audi', 'Mercedes', 'BMW', 'Volkswagen', 'Volvo'], 'Models': ['A5', 'XM', 'X5', 'Passat', 'V90']}

df = pd.DataFrame(data)

print(df)