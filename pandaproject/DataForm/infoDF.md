DataFrame: is a two dimensional data structure columns and row

Features of DataFrame:
-	Potentially columns are of different types.
-	Size - Mutable
- 	labeles as (row and columns)
- 	Can perform arithmetic operationas on row and columns


Example:

pandas.DataFrame

We can create pandas DataFrame follwoing:

pandas.DataFrame( data, index, columns, dtype, copy)

data 	= Data like ndarray, series, map, lists, dict, constants and another DataFrame.
index 	= Row labels, the index to be used for the resulting frame is Optional default: np.arange(n) if no index is passed
columns = Column labels, the optional default syntax is np.arange(n). This is true if no index is passed. 
dtype	= Data type for each column
copy	= This command or whatever it's used for copy data, if the default is False