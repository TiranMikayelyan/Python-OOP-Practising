class test:

    def __init__(self, name, card_code, salary):
        self.name = name 
        self.__card_code = card_code
        self._salary = salary

    def get_code(self): #getter private-ի արժեքը տեսնելու միջոց
        return self.__card_code
    
    def set_code(self, code): #setter private-ի արժեքը փոխելու միջոց
        self.__card_code = code
        return self.__card_code 

t = test("Olivier", 2020, 500000)

print(t.get_code())
print(t.set_code(2025))


        
