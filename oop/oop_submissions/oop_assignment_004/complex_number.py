import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
        if type(self.real_part)==str:
            if type(self.imaginary_part)==str:
                raise ValueError("Invalid value for real and imaginary part")
            else:
                raise ValueError("Invalid value for real part")
        elif type(self.imaginary_part)==str:
            if type(self.real_part)==str:
                raise ValueError("Invalid value for real and imaginary part")
            else:
                raise ValueError("Invalid value for imaginary part")
                
    def __str__(self):
        if self.imaginary_part>=0:
            return "{}+{}i".format(self.real_part,self.imaginary_part)
        else:
            return "{}{}i".format(self.real_part,self.imaginary_part)
            
    def conjugate(self):
        return ComplexNumber(self.real_part,-1*self.imaginary_part)
        
    def __add__(self,other):
        real1=self.real_part+other.real_part
        imaginary1=self.imaginary_part+other.imaginary_part
        return ComplexNumber(real1,imaginary1)
        
    def __sub__(self,other):
        real1=self.real_part-other.real_part
        imaginary1=self.imaginary_part-other.imaginary_part
        return ComplexNumber(real1,imaginary1)

    
    def __mul__(self,other):
        real1=self.real_part*other.real_part-self.imaginary_part*other.imaginary_part
        imaginary1=self.real_part*other.imaginary_part+self.imaginary_part*other.real_part
        return ComplexNumber(real1,imaginary1)
 
    def __truediv__(self,other):
        k=float(other.real_part**2+other.imaginary_part**2)
        real1=(self.real_part*other.real_part+self.imaginary_part*other.imaginary_part)/k
        imaginary1=(self.imaginary_part*other.real_part-self.real_part*other.imaginary_part)/k
        return ComplexNumber(real1,imaginary1)

    def __abs__(self):
        return round(math.sqrt(self.real_part**2+self.imaginary_part**2),3)
        
    def __eq__(self,other):
        return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part

        
        



            
            