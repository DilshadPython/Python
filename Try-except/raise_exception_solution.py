def make_delim_line(list_to_join, delim):
    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError('make_delim_line(): arg 1 must be a list or tuple')
    return formatted_line


# create > TypeError: can only join an iterable
find_line = make_delim_line(100, ',')
