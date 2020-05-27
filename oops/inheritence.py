''''class Employee:
    def __init__(self,name,id,phone_number):
        self.name=name
        self.id=id
        self.phone_number=phone_number
    
emp=Employee("swetha","R151616","7036437166")

class Developer(Employee):  
    def __init__(self,name,id,phone_number,programming):
        super().__init__(name,id,phone_number)
        self.programming=programming
        
class Manager(Employee):
    def __init__(self,name,id,phone_number,employee=None):
        super().__init__(name,id,employee)
        if employee==None:
            self.employee=[]
        else:
            self.employee=employee
    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
    
    def print_emp(self):
        for emp in self.employee:
            print("--->",emp.name)
emp1=Developer("Madhuri","R151652","9100767970","CLanguage")
emp2=Developer("Sai","R151652","9100767970","CLanguage")
agr=Manager("Swetha","R151618","7036437166",[emp1])
#print(agr.name)

agr.add_emp(emp2)

agr.remove_emp(emp1)
agr.print_emp()

#print(emp1.name)'''
sai-swetha-mathamsetti:~/environment $ ipython
Python 3.6.8 (default, Oct 14 2019, 21:22:53) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: class Parent: 
   ...:     x=1 
   ...:     def __init__(self): 
   ...:         self.y=2 
   ...:     def hello(): 
   ...:         print("Hello from Parent") 
   ...: class Child(Parent): 
   ...:     z=3 
   ...:                                                                                                                                    

In [2]: p,c=Parent(),Child()                                                                                                               

In [3]: p.x,p.y                                                                                                                            
Out[3]: (1, 2)

In [4]: p.hello()                                                                                                                          


In [5]: c.x,c.y,c.z                                                                                                                        
Out[5]: (1, 2, 3)

In [6]: Parent.x                                                                                                                           
Out[6]: 1

In [7]: Child.x                                                                                                                            
Out[7]: 1

TypeError: hello() takes 0 positional arguments but 1 was given

In [13]: class Parent: 
    ...:     x=1    
    ...:     def __init__(self): 
    ...:         self.y=2 
    ...:     def hello(self): 
    ...:         print("Hello from Parent") 
    ...: class Child(Parent): 
    ...:     z=3 
    ...:                                                                                                                                   

In [14]: a=Parent()                                                                                                                        

In [15]: a.hello()                                                                                                                         
Hello from Parent

In [16]:          
    sai-swetha-mathamsetti:~/environment $ ipython
Python 3.6.8 (default, Oct 14 2019, 21:22:53) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: class Dog: 
   ...:     species="Mammal" 
   ...:     def __init__(self,name,age): 
   ...:         self.name=name 
   ...:         self.age=age 
   ...:                                                                                                                                    

In [2]: a=Dog()                                                                                                                            
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-ebae484e6a80> in <module>
----> 1 a=Dog()

TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'

In [3]: a=Dog("Puppy",10)                                                                                                                  

In [4]: a.species                                                                                                                          
Out[4]: 'Mammal'

In [5]: class Dog: 
   ...:     species="Mammal" 
   ...:     def __init__(self,name,age): 
   ...:         self.name=name 
   ...:         self.age=age 
   ...:                                                                                                                                    

In [6]: class Dog: 
   ...:     pass 
   ...:                                                                                                                                    

In [7]: Dog()                                                                                                                              
Out[7]: <__main__.Dog at 0x7effcd537400>

In [8]: Dog()                                                                                                                              
Out[8]: <__main__.Dog at 0x7effcd521390>

In [9]: a=Dog()                                                                                                                            

In [10]: b=Dog()                                                                                                                           

In [11]: a==b                                                                                                                              
Out[11]: False

In [12]: class Dog(): 
    ...:     pass 
    ...:                                                                                                                                   

In [13]: a=Dog()                                                                                                                           

In [14]: type(a)                                                                                                                           
Out[14]: __main__.Dog

In [15]: class Dog: 
    ...:     species="Mammal" 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:                                                                                                                                   

In [16]: a=Dog("Puppy",10)                                                                                                                 

In [17]: b=Dog("Spudy",11)                                                                                                                 

In [18]: b.name                                                                                                                            
Out[18]: 'Spudy'

In [19]: if a.species=="Mammal"                                                                                                            
  File "<ipython-input-19-cf546a1f4ed2>", line 1
    if a.species=="Mammal"
                          ^
SyntaxError: invalid syntax


In [20]: if a.species=="Mammal": 
    ...:     print("True") 
    ...:                                                                                                                                   
True

In [21]: class Dog: 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:     def get_biggest_number(): 
    ...:         pass 
    ...:                                                                                                                                   

In [22]: a=Dog("Sudha",12)                                                                                                                 

In [23]: b=Dog("Bhanu",14)                                                                                                                 

In [24]: c=Dog("MadhuKumar",15)                                                                                                            

In [25]: class Dog: 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:     
    ...:                                                                                                                                   

In [26]: a=Dog("Sudha",12)                                                                                                                 

In [27]: b=Dog("Bhanu",14)                                                                                                                 

In [28]: c=Dog("MadhuKumar",15)                                                                                                            




In [30]: def get_biggest_number(*args): 
    ...:     print(args) 
    ...:                                                                                                                                   

In [31]: def get_biggest_number(*args): 
    ...:     print(max(args)) 
    ...:      
    ...:                                                                                                                                   

In [32]: def get_biggest_number(*args): 
    ...:     return (max(args)) 
    ...:      
    ...:      
    ...:                                                                                                                            

In [34]: get_biggest_number(12,13,14)                                                                                                      
Out[34]: 14

In [35]: class Dog: 
    ...:     species="Mammal" 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:     def description(self): 
    ...:         return "{} is {} years old".format(a.name,a.years) 
    ...:     def speak(self,sound): 
    ...:         return "{} says {}".format(a.name,sound) 
    ...:                                                                                                                                   

In [36]: a=Dog("Puppy",10)        
sai-swetha-mathamsetti:~/environment $ ipython
Python 3.6.8 (default, Oct 14 2019, 21:22:53) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: class Email: 
   ...:     def __init__(self): 
   ...:         self.is_sent=False 
   ...:     def is_sent(self): 
   ...:         self.is_sent=True 
   ...:                                                                                                                                    

In [2]: e=Email()                                                                                                                          

In [3]: e.is_sent()                                                                                                                        
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-63adc76a0f4f> in <module>
----> 1 e.is_sent()

TypeError: 'bool' object is not callable

In [4]: e.is_sent                                                                                                                          
Out[4]: False

In [5]: class Email: 
   ...:     def __init__(self): 
   ...:         self.is_sent=False 
   ...:     def is_send(self): 
   ...:         self.is_sent=True 
   ...:                                                                                                                                    

In [6]: e=Email()                                                                                                                          

In [7]: e.is_sent                                                                                                                          
Out[7]: False

In [8]: e.is_send()                                                                                                                        

In [9]: e.is_sent                                                                                                                          
Out[9]: True

In [10]: class Dog: 
    ...:     def __init__(self,breed): 
    ...:         self.breed=breed 
    ...:                                                                                                                                   

In [11]: spencer=Dog("German shepard")                                                                                                     

In [12]: spencer.breed                                                                                                                     
Out[12]: 'German shepard'

In [13]: class Dog: 
    ...:     species="Mammal" 
    ...:     def __init__(self,name,age)                                                                                                   
  File "<ipython-input-13-7d583bb82550>", line 3
    def __init__(self,name,age)
                               ^
SyntaxError: invalid syntax


In [14]: class Dog: 
    ...:     species="Mammal" 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:     def description(self): 
    ...:         return "{} is {} years old".format(self.name,self.age) 
    ...:     def speak(self,sound): 
    ...:         return "{} speaks like {}".format(self.name,self.sound) 
    ...:                                                                                                                                   

In [15]: class Puppy(Dog): 
    ...:     def run(self,speed): 
    ...:         return "{} runs {} kms".format(self.name,self.speed) 
    ...:                                                                                                                                   

In [16]: d=Dog("Kukka",12)                                                                                                                 

In [17]: d.name                                                                                                                            
Out[17]: 'Kukka'

In [18]: d.description()                                                                                                                   
Out[18]: 'Kukka is 12 years old'

In [19]: d.speak("Bow Bow")                                                                                                                
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-19-1c71c2735f9a> in <module>
----> 1 d.speak("Bow Bow")

<ipython-input-14-94aa83efaa9b> in speak(self, sound)
      7         return "{} is {} years old".format(self.name,self.age)
      8     def speak(self,sound):
----> 9         return "{} speaks like {}".format(self.name,self.sound)
     10 

AttributeError: 'Dog' object has no attribute 'sound'

In [20]: class Dog: 
    ...:     species="Mammal" 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:     def description(self): 
    ...:         return "{} is {} years old".format(self.name,self.age) 
    ...:     def speak(self,sound): 
    ...:         return "{} speaks like {}".format(self.name,sound) 
    ...:          
    ...:                                                                                                                                   

In [21]: d=Dog("Kukka",12)                                                                                                                 

In [22]: d.description()                                                                                                                   
Out[22]: 'Kukka is 12 years old'

In [23]: d.speak("Bow Bow")                                                                                                                
Out[23]: 'Kukka speaks like Bow Bow'

In [24]: class Dog: 
    ...:     species="Mammal" 
    ...:     def __init__(self,name,age): 
    ...:         self.name=name 
    ...:         self.age=age 
    ...:     def description(self): 
    ...:         return "{} is {} years old".format(self.name,self.age) 
    ...:     def speak(self,sound): 
    ...:         return "{} speaks like {}".format(self.name,sound) 
    ...:          
    ...:                                                                                                                                   

In [25]: class jhomby(Dog): 
    ...:     def run(self,speed): 
    ...:         return "{} speed is {}".format(self.name,speed) 
    ...:                                                                                                                                   

In [26]: d=Dog("Pup"",12)                                                                                                                  
  File "<ipython-input-26-b55274a5cf74>", line 1
    d=Dog("Pup"",12)
                    ^
SyntaxError: EOL while scanning string literal


In [27]: d=Dog("Pup",12)                                                                                                                   

In [28]: d.description()                                                                                                                   
Out[28]: 'Pup is 12 years old'

In [29]: d.speak("Bow Bow")                                                                                                                
Out[29]: 'Pup speaks like Bow Bow'

In [30]: j=jhomby()                                                                                                                        
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-30-f505d3472dbd> in <module>
----> 1 j=jhomby()

TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'

In [31]: j=jhomby("fgre",11)                                                                                                               

In [32]: j.description()                                                                                                                   
Out[32]: 'fgre is 11 years old'

In [33]: j.run(50)                                                                                                                         
Out[33]: 'fgre speed is 50'

In [34]: isstance(j,jhomby)                                                                                                                
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-34-264223d9ccd8> in <module>
----> 1 isstance(j,jhomby)

NameError: name 'isstance' is not defined

In [35]: isinstance(j,jhomby)                                                                                                              
Out[35]: True

In [36]: isinstance(d,jhomby)                                                                                                              
Out[36]: False

In [37]: isinstance(j,jhomby)                                                                                                              
Out[37]: True

In [38]: isinstance(j,dog)                                                                                                                 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-38-69df2edd0775> in <module>
----> 1 isinstance(j,dog)

NameError: name 'dog' is not defined

In [39]: isinstance(j,Dog)                                                                                                                 
Out[39]: True

In [40]: isinstance(j,Dog)                                                                                                                 

































                                                                                                                                           