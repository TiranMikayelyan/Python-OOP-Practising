class Transport:
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def main(self):
        print(f"{self.name} is moving at {self.speed} km/h")
    

class Car(Transport):
    
    def __init__(self, name, speed, seatscount):
        super().__init__(name, speed) #աշխատում է MRO-ով(Method Resolution Order)վերցնում է  հաջորդ կլասսը կանչում է constructor 
        self.seatscount = seatscount
    
    def info_Car(self):
        print(f"{self.name} has {self.seatscount} seats")
    
class Bike(Transport):

    def __init__(self, name, speed, company):
        #super().__init__(name, speed)
        Transport.__init__(self, name, speed) #ժառանգումը կազմակերպելու ձև , բայց առանց MRO, բազմաժառանգման ժամանակ վտանգավոր է
        self.company = company
    
    def info_bike(self):
        print(f"{self.name} related to {self.company} company")
    
#exemplars

car1 = Transport("Bus", 50)
car2 = Car("Hummer", 180, 5)
car3 = Bike("Bike", 20, "BMW" )

car1.main()
#car1.info_Car() չի աշխատի քանի որ ժառանգի մեթոդը ծնողի մեթոդ չի հանդիսանում

car2.main()
car2.info_Car()
#car2.info_bike() # Ժառանգը ժառանգից չի կարող մեթոդ վերցնել


car3.main()
car3.info_bike()
#car3.info_Car()# Ժառանգը ժառանգից չի կարող մեթոդ վերցնել

print(Bike.mro())
print(Car.mro())


