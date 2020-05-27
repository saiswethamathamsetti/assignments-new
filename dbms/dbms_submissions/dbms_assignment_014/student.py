class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score

               

    @staticmethod
    def filter(**kwargs):
        l=[]
        #list1=['student_id','name','age','score','student_id__lt','age__lt','score__lt','student_id__lte','age__lte','score__lte','student_id__gt','age__gt','score__gt','student_id__gte','age__gte','score__gte','age__neq','student_id__neq','score__neq','age__in','name__in','score__in','student_id__in','name__contains']
        d={'neq':'!=','gt':'>','gte':'>=','lt':'<','lte':'<=','in':'in','contains':'contains'}
             
        for k,v in kwargs.items():
             list1=['student_id','name','age','score']

             key=k.split("__")
             if key[0] not in list1:
                 raise InvalidField
             if len(key)==1:
                 condition=f"{k}='{v}'"
             elif key[1]=="contains": 
                 condition=f"{key[0]} like '%{v}%'"
             elif key[1]=="in":
                 condition=f"{key[0]} {d[key[1]]} {tuple(v)}"

             else:
                 condition=f"{key[0]} {d[key[1]]} '{v}'"
             l.append(condition)
             p=" and ".join(l)
             query=" "+p
        #print(query)
        return query
             
    
    
    @classmethod
    def avg(cls, field, **kwargs):
        list1=['student_id','name','age','score']
        if field not in list1:
            raise InvalidField
        if len(kwargs)>=1:
            p=Student.filter(**kwargs)
            query=f"select avg({field}) from Student where {p}"
        else:
            query=f"select avg({field}) from Student"
        return read_data(query)[0][0]
    @classmethod
    def min(cls, field, **kwargs):
        list1=['student_id','name','age','score']
        if field not in list1:
            raise InvalidField
        if len(kwargs)>=1:
            p=Student.filter(**kwargs)
            query=f"select min({field}) from Student where {p}"
        else:
            query=f"select min({field}) from Student"
        return read_data(query)[0][0]
    @classmethod
    def max(cls, field, **kwargs):
        list1=['student_id','name','age','score']
        if field not in list1:
            raise InvalidField
        if len(kwargs)>=1:
            p=Student.filter(**kwargs)
            query=f"select max({field}) from Student where {p}"
        else:
            query=f"select max({field}) from Student"
        return read_data(query)[0][0]
    @classmethod
    def sum(cls, field, **kwargs):
        list1=['student_id','name','age','score']
        if field not in list1:
            raise InvalidField
        if len(kwargs)>=1:
            p=Student.filter(**kwargs) 
            query=f"select sum({field}) from Student where {p}"
        else:
            query=f"select sum({field}) from Student"
        return read_data(query)[0][0]
        
    @classmethod
    def count(cls, field=None, **kwargs):
        list1=['student_id','name','age','score']
        if field==None:
            query="select count() from Student"
        elif field not in list1:
            raise InvalidField
        elif len(kwargs)>=1:
            p=Student.filter(**kwargs)
            query=f"select count({field}) from Student where {p}"
        else:
            query=f"select count({field}) from Student"
        return read_data(query)[0][0]






        
    








    

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
	
#s = Student.filter(age__lt=30,score__gt=28)
#avg_age = Student.avg('age', age__gt=18)
#print(avg_age)