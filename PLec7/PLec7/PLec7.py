#class A :
#    def __init__(self):
#        print("A 생성자 호출")
#class B :
#    def __init__(self):
#        print("B 생성자 호출")
#class C(A,B) :
#    def __init__(self):
#        A.__init__(self)
#        B.__init__(self)
#        print("C 생성자 호출")

#c = C()




#from abc import ABCMeta, abstractmethod

#class Terran(metaclass=ABCMeta):
#    def __init__(self, name):
#        self.name = name
    
#    @abstractmethod
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self, name, demage):
#        super().__init__(name)
#        self.demage = demage

#    def attack(self):
#        print("탱크를 쏘았다!")

#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(name)
#        self.hp = hp

#    def attack(self):
#        print("총을 쏘았다!")

#def attack(terran):
#    terran.attack()

#t1 = Tank("tank", 0)
#t2 = Marine("marine", 100)

#tlist = [Tank("tank1", 0), Tank("tank2", 0), Marine("marine1", 100)]
#for item in tlist:
#    attack(item)




class MyList(list):
    name = ""
    def __init__(self, name):
        super().__init__([])
        self.name = name

    def __str__(self):
        return self.name+":"+super().__str__()

list1 = MyList("jihae")
list1.append(10)
list1.append(50)
list1.append(20)
list1.append(70)
list1.append(90)
list1.append(100)

print(list1)


