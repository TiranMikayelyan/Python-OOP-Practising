import datetime
class example:

    raise_percent = 1.2 #class atribute

    def __init__(self, firstname, lastname, salary ): #self = object
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + lastname + "@gmail.com"

    def firstname(self):
        return "{} {}".format(self.firstname,self.lastname)

    def pay(self):
        return "{} {}".format(self.firstname,self.salary)
    
    def raise_salary(self):
        self.salary = self.salary * example.raise_percent
        return "{} {}".format(self.firstname , self.salary)
    
    #classmethods works with class
    @classmethod
    def formation(cls, str):
        firstname, lastsname, pay = str.split('-')
        return cls(firstname,lastsname,pay)
    
    @staticmethod #they aren't depend from classes
    def is_workday(day):
        if day.weekday() == 6 or day.weekday() == 7:
            return False
        else:
            return True



# test1 = example("Oscar", "Bob", 5500) #exemplar-> example("Oscar", "Bob", 5500)  test1-> object
# test2 = example("Romeo", "Santos", 4000)

# print(example.firstname(test1))
# print(example.pay(test1))

# print(test.pay) #old
# test1.raise_salary() #method call
# print(test.pay) #new

# test1.raise_percent = 1.5 #object atribute
# print(test1.raise_salary()) #new


# print(example.raise_percent)
# print(test1.raise_percent)
# print(test2.raise_percent)


# print(test1.__dict__)
# print(example.__dict__)

#classmethods
example1 = "John-Green-8000"
example2 = "Jack-London-1000"

new_test = example.formation(example1)
print(new_test.email)
print(new_test.salary)

#statichmethods
my_date = datetime.date(2003,1,1)
print(example.is_workday(my_date))
