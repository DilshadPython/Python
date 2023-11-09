import numpy as np
import pandas as pd


car_ser = pd.Series(['a','b','v','f','p'], ['Audi','BMW','Volvo','Ford','Porshe'])
print(car_ser)

print(car_ser[1:3])

print(car_ser[0:4])

print(car_ser[1:3] + car_ser[0:4])