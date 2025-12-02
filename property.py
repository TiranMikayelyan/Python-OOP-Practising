class test:

    def __init__(self, name, card_code, salary):
        self.name = name 
        self.__card_code = card_code
        self._salary = salary

    @property 
    # property-ը ավելի ապահով է, որովհետև attribute-ին ուղղակի չեն դիպչում,
    # այլ անցնում են getter-ի միջով. Կարող ես validation, checks, permissions դնել
    def code(self):                      # getter → private արժեքը կարդալու միջոց
        return self.__card_code
    
    @code.setter
    # setter-ը նույնպես անցնում է control-ի միջով.
    # Սա ապահովում է, որ սխալ տվյալ չանցնի (օր.՝ բացասական կամ սխալ տիպ)
    def code(self, pin):                 # setter → private արժեքը փոխելու միջոց
        self.__card_code = pin

t = test("Olivier", 2020, 500000)

print(t.code) #getter-ը աշխատեց
t.code = 2855 #setter-ը կփոխի արժեքը

print(t.code) 

t._test__card_code = 5555
print(t._test__card_code)

print(t.code) # կտպի նոր արժեքը



        
