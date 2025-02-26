def msg(n: int) -> str:
    """
    The docstring is this comment write here.
    msg n times

    :param n: Number of times to msg
    :type n :int
    :raise TypeError: If n is not an integer.
    :return: A string of msg n times, one per line.
    :rtype: str
    """
    return f"Hello, docstring\n" * n

num: int = int(input('Enter a number: '))
msg: str = msg(num)
print('-> ', msg, end='')