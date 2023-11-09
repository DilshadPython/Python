def make_delim_line(list_to_join, delim):
	formatted_line = delim.join(list_to_join)
	return formatted_line

# create > TypeError: can only join an iterable
find_line = make_delim_line(100, ',')