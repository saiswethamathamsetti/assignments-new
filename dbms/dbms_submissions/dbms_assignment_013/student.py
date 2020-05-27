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
        
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)

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
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;") 
        if self.student_id==None:
            crsr.execute("INSERT INTO Student (name,age,score) VALUES('{}',{},{})".format(self.name,self.age,self.score)) 
            self.student_id=crsr.lastrowid
        
        else:
            if self.check1(self.student_id):
                crsr.execute("UPDATE Student SET name='{}',age={},score={} WHERE student_id={}".format(self.name,self.age,self.score,self.student_id))
            else:
                if self.check1(self.student_id):
                    crsr.execute("UPDATE Student SET name='{}',age={},score={} WHERE student_id={}".format(self.name,self.age,self.score,self.student_id))
                else:
                    crsr.execute("INSERT INTO Student(student_id,name,age,score) VALUES({},'{}',{},{})".format(self.student_id,self.name,self.age,self.score))  
        
        connection.commit()   
        connection.close()
        
    


    
    @staticmethod    
    def filter(**kwargs):
       
        list1=['student_id','name','age','score','student_id__lt','age__lt','score__lt','student_id__lte','age__lte','score__lte','student_id__gt','age__gt','score__gt','student_id__gte','age__gte','score__gte','age__neq','student_id__neq','score__neq','age__in','name__in','score__in','student_id__in','name__contains']
       
        for k,v in kwargs.items():
            if k=="student_id":
                data1=read_data("SELECT * FROM Student WHERE student_id={}".format(v))
            elif k=="name":
                data1=read_data("SELECT * FROM Student WHERE name='{}'".format(v))
            elif k=="age":
                data1=read_data("SELECT * FROM Student WHERE age={}".format(v))
            elif k=="score":
                data1=read_data("SELECT * FROM Student WHERE score={}".format(v))
            elif k=="age__lte":
                data1=read_data("SELECT * FROM Student WHERE age<={}".format(v))
            elif k=="age__lt":
                data1=read_data("SELECT * FROM Student WHERE age<{}".format(v))
            elif k=="age__gte":
                data1=read_data("SELECT * FROM Student WHERE age>={}".format(v))
            elif k=="age__gt":
                data1=read_data("SELECT * FROM Student WHERE age>{}".format(v))
            elif k=="student_id__lte":
                data1=read_data("SELECT * FROM Student WHERE student_id<={}".format(v))
            elif k=="student_id__lt":
                data1=read_data("SELECT * FROM Student WHERE student_id<{}".format(v))
            elif k=="student_id__gte":
                data1=read_data("SELECT * FROM Student WHERE student_id>={}".format(v))
            elif k=="student_id__gt":
                data1=read_data("SELECT * FROM Student WHERE student_id>{}".format(v))
            elif k=="age__neq":
                data1=read_data("SELECT * FROM Student WHERE age<>{}".format(v))
            elif k=="student_id__neq":
                data1=read_data("SELECT * FROM Student WHERE student_id<>{}".format(v))
            elif k=="score__lt":
                data1=read_data("SELECT * FROM Student WHERE score<{}".format(v))
            elif k=="score__lte":
                data1=read_data("SELECT * FROM Student WHERE score<={}".format(v))
            elif k=="score__gt":
                data1=read_data("SELECT * FROM Student WHERE score>{}".format(v))
            elif k=="score__gte":
                data1=read_data("SELECT * FROM Student WHERE score>={}".format(v))
            elif k=="score__neq":
                data1=read_data("SELECT * FROM Student WHERE score<>{}".format(v))
            elif k=="name__contains":
                data1=read_data("SELECT * FROM Student WHERE name LIKE '%{}'".format(v))
            elif k=="score__in":
                v=tuple(v)
                data1=read_data("SELECT * FROM Student WHERE score in {}".format(v))
            elif k=="student_id__in":
                v=tuple(v)
                data1=read_data("SELECT * FROM Student WHERE student_id in {}".format(v))
            elif k=="name__in":
                v=tuple(v)
                data1=read_data("SELECT * FROM Student WHERE name in {}".format(v))
            elif k=="name__neq":
                data1=read_data("SELECT * FROM Student WHERE name<>'{}'".format(v))
            elif k=="age__in":
                v=tuple(v)
                data1=read_data("SELECT * FROM Student WHERE age in {}".format(v))
                
            elif k not in list1:
                raise InvalidField
                
            l1=[]
            
            if len(data1)==0:
                return l1
            
            else:
                for i in range(0,len(data1)):
                    final=Student(data1[i][1],data1[i][2],data1[i][3])
                    final.student_id=data1[i][0]
                    l1.append(final)

        return l1
         
             

    
        
                    
            
    @staticmethod    
    def check1(student_id):
        data2=read_data("SELECT student_id FROM Student WHERE student_id={}".format(student_id))
        
        if len(data2)!=0:
            return True
        else:
            return False
    
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit()   
    connection.close()
        
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans
 