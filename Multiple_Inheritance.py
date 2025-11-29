class Transport:
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def main(self):
        print(f"{self.name} is moving at {self.speed} km/h")
    

class Car(Transport):
    
    def __init__(self, name, speed, seatscount, **kwargs):
        super().__init__(name, speed,**kwargs) #աշխատում է MRO-ով(Method Resolution Order)վերցնում է  հաջորդ կլասսը կանչում է constructor 
        self.seatscount = seatscount
    
    def info_Car(self):
        print(f"{self.name} has {self.seatscount} seats")
    
class Bike(Transport):

    def __init__(self, name, speed, company, **kwargs): #kwargs Որպեսզի յուրաքանչյուր կլաս ստանա իրեն պետք եկող argument–ները, իսկ ավելցուկ argument–ները ուղարկվեն հաջորդ կլասին (MRO–ով)։
        #super().__init__(name, speed)
        Transport.__init__(self, name, speed, **kwargs ) #ժառանգումը կազմակերպելու ձև , բայց առանց MRO, բազմաժառանգման ժամանակ վտանգավոր է
        self.company = company
    
    def info_bike(self):
        print(f"{self.name} related to {self.company} company")

class Motocar(Car,Bike):

    def __init__(self, name, speed, seatscount,company):
        super().__init__(name, speed,  seatscount=seatscount, company=company)


    
#exemplar

moto = Motocar("Scooter", 40, 1, "BYD")


moto.main()
moto.info_Car()
moto.info_bike()

print(Motocar.mro())


