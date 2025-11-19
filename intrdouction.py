class example:
    def __init__(self, firstname, lastname, salary ):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + lastname + "@gmail.com"

    def firstname(self):
        return "{} {}".format(self.firstname,self.lastname)

    def salary(self):
        return "{} {}".format(self.firstname,self.salary)
    
test1 = example("Oscar", "Bob", 5500)
print(example.firstname(test1))
print(example.salary(test1))

