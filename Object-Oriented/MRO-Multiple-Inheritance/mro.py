
class A(object):
    def do_this(self):
        print(' Do this in A')


class B(A):
    pass


class C(object):
    def do_this(self):
        print('Do this in C')


class D(B, C):
    pass


instance_obj = D()
instance_obj.do_this()

print(D.mro())
print('D > B > A > C')
