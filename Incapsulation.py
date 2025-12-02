class test:

    def __init__(self, name, card_code, salary):
        self.name = name
        self.__card_code = card_code #private
        self._salary = salary #protected


t = test("Olivier", 2020, 500000)

print("old")
print(t.name)
print(t._test__card_code) 
print(t._salary)

print("\n")

t.name = "James"
# t._test__card_code = 2003 #class-ը այստեղ կստեղծի նոր atribute ու կվերագրի 2003, իսկ իրական private atribute-ը պահվում է t._test__card_code տեսքով։
t._test__card_code = 2003
t._salary = 60000

print("new")
print(t.name)
print(t._test__card_code)
print(t._salary)




        
