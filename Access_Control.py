class A:
    
    def __init__(self,name, age, Number):
        self.name= name
        self._age = age
        self.__Number = Number

    def show(self):
        return "{} aged {} like the {} number".format(self.name, self._age, self.__Number)

class B(A):

    def __init__(self, name, age , number):
        super().__init__(name,age,number)



obj = A('Oscar', 32, 10)
obj1 = B('Karen', 22, 2)
#Public attribute-ը ժառանգի օբյեկտում նույնպես public է և լիովին հասանելի է դրսից
print("Old")
print(obj.name)
print(obj1.name)

print("\n")

#կարող ենք փոխել public atribute-ը

print("New")
obj.name = "Olivier"
obj1.name = "Colman"

print(obj.name)
print(obj1.name)

#Protected attribute-ը ժառանգին հասանելի է, բայց արտաքին օգտագործման համար նախատեսված չէ 
print("\n")

print("Old")
print(obj._age) 
print(obj1._age)

print("\n")

#դրսից կարող ենք փոխել
print("New")
obj._age = 18
obj1._age = 41

print(obj._age) 
print(obj1._age)

#private-ը ժառանգի օբյեկտի համար private է, էտ ատրիբուտին դրսից դիմել չենք կարող
#print(obj.__Number) 
#print(obj1.__Number)
print("\n")

"Python–ը __Number–ը name-mangling ա անում և փոխում ա անունը __Number → _A__Number"
#private-ը ժառանգի օբյեկտի համար private է էտ ատրիբուտին դիմել չենք կարող, բայց առաջանում է _A__Number որով կարող ենք դիմել
print("Old")
print(obj._A__Number)
print(obj1._A__Number)

print("\n")
print("New")

obj.__Number = 99
obj1.__Number = 100

# error Չի բայց չի էլ փոփոխվի
print(obj._A__Number)
print(obj1._A__Number)

print(obj.show())
print(obj1.show())
