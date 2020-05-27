class Employee:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname,self.lastname)
    @property
    def full_name(self):
        return '{} {}'.format(self.firstname,self.lastname)
emp1=Employee("Swetha","Mathamsetti")
emp1.firstname='Madhuri'
emp1.lastname='Vavilapalli'
print(emp1.firstname)
 
print(emp1.full_name)

print(emp1.email)

