class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
class Student:
    def __init__(self, name, age, score):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score

    @staticmethod
    def get(student_id=0,name="",age=0,score=-1,**kwargs):
        if  student_id!=0:
            data1=read_data("SELECT * FROM Student WHERE student_id={}".format(student_id))
        elif name!="":
            data1=read_data("SELECT * FROM Student WHERE name='{}'".format(name))
        elif age!=0:
            data1=read_data("SELECT * FROM Student WHERE age={}".format(age))
        elif score!=-1:
            data1=read_data("SELECT * FROM Student WHERE score={}".format(score))
        else:
            raise InvalidField
            
        if len(data1)==0:
            raise DoesNotExist
        elif len(data1)>1:
            raise MultipleObjectsReturned
        else:
            final=Student(data1[0][1],data1[0][2],data1[0][3])
            final.student_id=data1[0][0]
            return final
            
    def delete(self):
        data1=("DELETE FROM Student WHERE student_id={}".format(self.student_id))
        write_data(data1)
    
    def save(self):
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;") 
        if self.student_id==None:
            crsr.execute("INSERT INTO Student (name,age,score) VALUES('{}',{},{})".format(self.name,self.age,self.score)) 
            self.student_id=crsr.lastrowid
        else:
            crsr.execute("UPDATE Student SET name='{}',age={},score={} WHERE student_id={}".format(self.name,self.age,self.score,self.student_id))
        
        connection.commit()   
        connection.close()
        
        
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit()   
    connection.close()
        
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans
'''   
student_object = Student(name="Swetha",age=20,score=90)
#student_object.save()
a=student_object.get(student_id=1)
print(a.student_id)
print(a.name)
print(a.age)
print(a.score)
'''