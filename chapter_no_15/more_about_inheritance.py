# # is multiple inhertance possibale or not
# class A:
#     def __init__(self, a):
#         self.a = a

# class B:
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b

# class C(B,A):
#     def __init__(self, a,b,c):
#         super().__init__(a,b)
#         self.c = c

#     def display(self):
#         return f"a : {self.a} b : {self.b} c : {self.c}"


# obj = C(4,5,7)
# print(obj.display())

# # Multilevel inheretance
# class A:
#     def __init__(self, a):
#         self.a = a

# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b

# class C(B):
#     def __init__(self, a,b,c):
#         super().__init__(a,b)
#         self.c = c

#     def display(self):
#         return f"a : {self.a} b : {self.b} c : {self.c}"

# obj = C(4,5,7)
# print(obj.display())

# # Method overriding
# class A:
#     def display(self):
#         return f"this is class A"

# class B(A):
#     def display(self):
#         return f"This is class B"

# class C(B):
#     def display(self):
#         return f"This is class C"
# a = A()
# b = B()
# c = C()
# print(c.display())
# # method resolution order
# print(help(C))
# or
# print(C.mro())
# # isinstance: use to check that object is this class or not it give True or False(if that object is inherted then it give True)
# print(isinstance(c,C)) #True
# print(isinstance(c,B)) #True 
# print(isinstance(c,A)) #True
# print(isinstance(b,B)) #True
# print(isinstance(b,A)) #True
# print(isinstance(a,A)) #True
# print(isinstance(a,B)) #False
# print(isinstance(a,C)) #False

# # issubclass: use to check that class is subclass of other class or not
# print(issubclass(C,B))
# print(issubclass(C,A))
# print(issubclass(B,A))
# print(issubclass(A,B))
# print(issubclass(A,C))