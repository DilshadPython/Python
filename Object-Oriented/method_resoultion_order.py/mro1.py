'''
mro is a method resolution order which is tell how the inheritance class
works 
'''


class A(object):
    def do_this(self):
        print(' Do this in A')


class B(A):
    pass


class C(A):
    def do_this(self):
        print('Do this in C')


class D(B, C):
    pass


instance_obj = D()
instance_obj.do_this()

print(D.mro())
print('D > B > C > A')
