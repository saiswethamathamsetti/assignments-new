class Item:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        if self.price<=0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
        
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
        
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        operations=["IN","EQ","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
        self.operation=operation
        if operation not in operations:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
        self.value=value
        
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
        
class Store:
    def __init__(self):
        self.itemlist=[]

    def add_item(self,item):
        return self.itemlist.append(item)

    def count(self):
        return len(self.itemlist)
        
    def __str__(self):
        if len(self.itemlist)>0:
            return "\n".join(map(str,self.itemlist))
        else:
            return 'No items'  
            
    def filter(self,query):
        obj=Store()
        for i in self.itemlist:
            if query.operation=='EQ' and getattr(i,query.field)==query.value:
                obj.add_item(i)
            elif query.operation=='GT' and getattr(i,query.field)>query.value:
                obj.add_item(i)
            elif query.operation=='GTE' and getattr(i,query.field)>=query.value:
                obj.add_item(i)
            elif query.operation=='LT' and getattr(i,query.field)<query.value:
                obj.add_item(i)
            elif query.operation=='LTE' and getattr(i,query.field)<=query.value:
                obj.add_item(i)
            elif query.operation=='STARTS_WITH' and getattr(i,query.field).startswith(query.value):
                obj.add_item(i)
            elif query.operation=='ENDS_WITH' and getattr(i,query.field).endswith(query.value):
                obj.add_item(i)
            elif query.operation=='IN' and getattr(i,query.field) in query.value :
                obj.add_item(i)
            elif query.operation=='CONTAINS' and getattr(i,query.field).__contains__(query.value):
                obj.add_item(i)
        return obj
    
    def exclude(self,query):
        exclude_object=Store()
        include_object=self.filter(query)
        for i in self.itemlist:
            if i not in include_object.itemlist:
                exclude_object.add_item(i)
        return exclude_object
        
        
        
        
                        
            
    
