class example:

    raise_percent = 1.2 #class atribute

    def __init__(self, firstname, lastname, salary ): #self = object
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + lastname + "@gmail.com"

    def firstname(self):
        return "{} {}".format(self.firstname,self.lastname)

    def salary(self):
        return "{} {}".format(self.firstname,self.salary)
    
    def raise_salary(self):
        self.salary = self.salary * example.raise_percent
        return "{} {}".format(self.firstname , self.salary)



test1 = example("Oscar", "Bob", 5500) #exemplar-> example("Oscar", "Bob", 5500)  test1-> object
test2 = example("Romeo", "Santos", 4000)

print(example.firstname(test1))
print(example.salary(test1))

print(test1.salary) #old
test1.raise_salary() #method call
print(test1.salary) #new

test1.raise_percent = 1.5 #object atribute
print(test1.raise_salary()) #new


print(example.raise_percent)
print(test1.raise_percent)
print(test2.raise_percent)


print(test1.__dict__)
print(example.__dict__)


