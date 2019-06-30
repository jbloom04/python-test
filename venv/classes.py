class Student(object):
    __slots__ = ['name', 'identifier','age']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    # def myf(self):
    #     for prop in self.__dict__.values():
    #         print(prop)

class Student2(object):
    age = 38        #public property
    def __init__(self, name,n):
        self.__name = name
        self.__n = n

class A(object):
   def __init__(self,b,c):
     self.b = b
     self.c = c
   def do_nothing(self):
     pass

class dynamic():
    pass


