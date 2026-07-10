#Hierarchal Inheritance:

class O:
    pass

class A(O):
    pass

class B(O):
    pass

class C(O):
    pass

class A1(A):
    pass
class A2(A):
    pass
class A3(A):
    pass

class B1(B):
    pass
class B2(B):
    pass
class B3(B):
    pass

class C1(C):
    pass
class C2(C):
    pass
class C3(C):
    pass


"""
                                O
                                |
    ---------------------------------------------------------------
    |                           |                                 |
    A                           B                                 C
    |                           |                                 |
-----------               ----------------                ------------------
|   |     |               |     |        |                |        |       |
A1  A2    A3              B1    B2       B3               C1       C2      C3

"""
#Means in hierarchal inheritance we make subclasses(A,B,C) from a parent class(O), then we make separate sub-sub classes from that subclasses like (A1,A2,A3) from A, similarly for B and C. So, this is called hierarchal inheritance.


#Hybrid Inheritance:

class Human:
    pass

class Employee1(Human):
    pass

class Employee2(Human):
    pass

class Programmer(Employee1, Employee2):
    pass


"""
                            Human
                              |
    ------------------------------------------------------
    |                                                    |
    Employee1                                           Employee2
    |                                                    |
    \                                                    /
     \                                                  /
      \                                                /
       \                                              / 
        \                                            /
         \                                          /
          \----------------------------------------/
                                |
                            Programmer

"""

#Hybrid inheritance basically means this whole system will have both multiple and multilevel inheritance, multiple inheritance is when you make a subclass from two or more parent classes (which is the class programmer), multilevel inheritance is when you make a subclass from a parent class, then make a sub-sub class from the subclass (here Human ---> Employee1 or Employee2 ---> Programmer). So, this whole system of inheritance is called hybrid inheritance.