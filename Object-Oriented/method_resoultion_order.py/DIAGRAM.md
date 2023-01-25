# Method resolution order: mor

class A:
   ^
   |
   |
class B(A)    class C:
        ^       ^
         \     /
          \   /
           \ /      
        class D(B, C)

print(D.mro())
Do this in A
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
D > B > A > C


# Method resolution order 1: mor1

		class A:
       ^       ^    
      /         \
     /           \
class B(A)    class C:
        ^       ^
         \     /
          \   /
           \ /      
        class D(B, C)

print(D.mro())
Do this in C
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
D > B > C > A

