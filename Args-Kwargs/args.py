# (*args) is used to pass a non-keyworded, variable-length argument list,
# (**kwargs) is used to pass a keyworded, variable-length argument list.


def test_var_args(frag, *args):
    print('Start testing format of arg', frag)
    for arg in args:
        print('Here is arg', arg)


test_var_args(2, 9, 3)
