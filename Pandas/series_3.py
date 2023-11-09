import numpy as np
import pandas as pd


car_ser = pd.Series([1, 3, 6, 9, 4], ['Audi', 'BMW', 'Volvo', 'Ford', 'Porshe'])

car_ser1 = car_ser[2:]

print(car_ser1)

car_ser2 = car_ser[0:]

print(car_ser2)

print(car_ser1 + car_ser2)
