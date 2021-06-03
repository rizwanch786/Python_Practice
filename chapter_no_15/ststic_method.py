# Static method: is defined by @staticmethod decorator. There is not self argument is defined as a simple method.
class A:
    @staticmethod
    def hello():
        print ("Hi I'm Static Method")

a = A()
a.hello()
A.hello()
