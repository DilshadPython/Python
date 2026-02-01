import pandas as pd

df = pd.DataFrame()

print(df)

RangeIndex(start=0, stop=8, step=1)

=================== set_index ================

         Nums Car1    Car2  Names        Car4
Car3
MB-SLS     44   A1  BMW-06   Alan        F150
MB-CLA     56   A2  BMW-20    Tom      Ranger
MB-GLA     72   A3  BMW-24  Chris     Transit
MB-SL      98   S3  BMW-30    Ema   SuperDuty
MB-R231     2   A4  BMW-35   Dave  Expedition
MB-G63     76   A5  BMW-40    Sam        Edge
ML250      99   A6  BMW-45  Loren          FT
ML         76   A7  BMW-50   Kaio         FTT

===================== Head =====================

   Nums Car1    Car2     Car3  Names        Car4
0    44   A1  BMW-06   MB-SLS   Alan        F150
1    56   A2  BMW-20   MB-CLA    Tom      Ranger
2    72   A3  BMW-24   MB-GLA  Chris     Transit
3    98   S3  BMW-30    MB-SL    Ema   SuperDuty
4     2   A4  BMW-35  MB-R231   Dave  Expedition


 Convert Data Frame to Dictionary:

{'Nums': [44, 56, 72, 98, 2, 76, 99, 76],
 'Car1': ['A1', 'A2', 'A3', 'S3', 'A4', 'A5', 'A6', 'A7'],
 'Car2': ['BMW-06', 'BMW-20', 'BMW-24', 'BMW-30', 'BMW-35', 'BMW-40', 'BMW-45', 'BMW-50'],
 'Car3': ['MB-SLS', 'MB-CLA', 'MB-GLA', 'MB-SL', 'MB-R231', 'MB-G63', 'ML250', 'ML'],
 'Names': ['Alan', 'Tom', 'Chris', 'Ema', 'Dave', 'Sam', 'Loren', 'Kaio'],
 'Car4': ['F150', 'Ranger', 'Transit', 'SuperDuty', 'Expedition', 'Edge', 'FT', 'FTT']}
