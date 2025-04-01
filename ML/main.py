import pandas as pd
import quandl

df = quandl.get('EOD/GOOGLE', authtoken='...')
