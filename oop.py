'''class Person:
    pass
from oop import Person
swetha=Person()
print(swetha)
print(type(swetha))
if type(swetha)==Person:
    print("True")
else:
    print("False")'''
'''class Person:
    def say_hello(self):
        print("Hello")
        print(self)
from oop import Person
swetha=Person()
swetha.say_hello()'''
'''class Person:
    def say_hello(self,name='Swetha'):
        return "Hello {}".format(name)
from oop import Person
swetha=Person()
k=swetha.say_hello()
print(k)'''


'''class Person:
    def __init__(self,name):
        print("Hello I'm {}".format(name))
    def say_hello(self):
        print("Hello")

#from oop import Person
p=Person("Swetha")'''

#single attribute
'''class Person:
    def __init__(self,full_name):
        self.name=full_name
p=Person("Swetha")
print(p.name)'''

'''class Person:
    def __init__(self,full_name,place):
        self.name=full_name
        self.location=place
    def say_hello(self):
        print("Hello I'm {}".format(self.name))
p=Person("Swetha","Amalapuram")
p.say_hello()
print(p.name)
print(p.location)'''

'''class Car:
    def __init__(self,color,acceleration):
        self.color=color
        self.acceleration=acceleration
        self.speed=0
    def accelerate(self):
        print("Speeding Up")
        self.speed+=self.acceleration
    def apply_breaks(self):
        print("Applying Breaks")
        self.speed-=10
p=Car("Pink",60)
p.accelerate()
p.apply_breaks()
print(p.acceleration)
print(p.speed)'''

'''class BankAccount:
    def __init__(self,name,mobile_no):
        self.name=name
        self.mobile_no=mobile_no
        self.generate_account_no()
        self.balance=0
    def generate_account_no(self):  
        import uuid
        self.account_no=str(uuid.uuid4())
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient amount")
        else:
            self.balance-=amount
b=BankAccount("Swetha","7036437166")
b.generate_account_no()
b.deposit(1000)
b.withdraw(200000)
print(b.balance)
print(b.name)
print(b.mobile_no)
print(b.account_n)'''

'''def __str__(self):
    return self.color'''

'''class Bike:
    def __init__(self,color):
        self.color=color
        self.acceleration=0
    def accelerate(self):
        self.acceleration+=10
    def __str__(self):
        return self.color
bike=Bike("Blue")
bike.accelerate()
print(bike)'''


'''class Employee:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname,self.lastname)
    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    
    @fullname.setter
    def fullname(self,name):
        firstname,lastname=name.split(" ")
        self.firstname=firstname
        self.lastname=lastname
    @fullname.deleter
    def fullname(self):
        print("DeleteName")
        self.firstname=None
        self.lastname=None
emp_1=Employee("Swetha","Mathamsetti")
#emp_1.firstname="Madhuri"
emp_1.fullname='Saiswetha Mathamsetti'

print(emp_1.email)
del emp_1.fullname
print(emp_1.fullname)'''


'''class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient Amount")
    def print_balance(self):
        return self.balance
            
bankbalance=BankAccount()
bankbalance.deposit(100)
bankbalance.deposit(400)
print(bankbalance.print_balance())
bankbalance.withdraw(200)
print(bankbalance.print_balance())'''

'''class Hello: 
    def __init__(self):
        self.a=1  
        self.b=2
        self.__c=3
    def private_method(self):
        print(self.__c)
        self.__private_met()
    def __private_met(self):
        print("private method")
hello=Hello()
print(hello.a)
print(hello.b)
hello.private_method()'''


'''class A:
    def feature1(self):
        print("Feature1")
    def feature2(self):
        print("Feature2")
class B:
    def feature3(self):
        print("Feature3")
    def feature4(self):
        print("Feature4")
class C(A,B):
    def feature5(self):
        print("Feature5")'''
        

class MyEditor:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell Check")
        print("Convention Check")



class Laptop:
    def code(self,ide):
        ide.execute()
ide = MyEditor()
lap1=Laptop()
lap1.code(ide)
        





















    












































































        
        
        
        
        
        



































