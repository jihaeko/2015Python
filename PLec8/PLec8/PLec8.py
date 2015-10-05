#class A(): 
#    def __init__(self, a): 
#        self.a = a 
#    def show(self): 
#        print('show a:', self.a) 
        
#class B(A):
#    def __init__(self, b, **arg):
#        super().__init__(**arg)
#        self.b = b
#    def show(self):
#        print('show b:', self.b)
#        super().show()

#class C(A):
#    def __init__(self, c, **arg):
#        super().__init__(**arg)
#        self.c = c
#    def show(self):
#        print('show c:', self.c)
#        super().show()

#class D(B,C):
#    def __init__(self, d, **arg):
#        super().__init__(**arg)
#        self.d = d
#    def show(self):
#        print('show d:', self.d)
#        super().show()

#data = D(a=1, b=2, c=3, d=4)
#data.show()


#Private관련
#
#class Mapping:
#    def __init__(self, iterable):
#        self.items_list = []
#        self.__update(iterable)

#    def update(self, iterable):
#        for item in iterable:
#            self.items_list.append(item)

#    #private copy of original update() method
#    #내 멤버로다가 만들자! 
#    __update = update

#class MappingSubclass(Mapping):

#    def update(self, keys, values):
#        # provides new signature for update()
#        # but does not break __init__()
#        for item in zip(keys, values):
#            self.items_list.append(item)

#data = MappingSubclass(['hi', 'bye'])
#print(data.items_list)

#data.update([1, 2, 3], [10, 20, 30])
#print(data.items_list)



import sys
number1 = float(input("enter a number:"))
number2 = float(input("enter a number:"))
try:
    result = number1/number2
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("The answer is infinity")
except:
    error = sys.exc_info()[0]
    print(error)
    sys.exit()
finally:
    print("Done")