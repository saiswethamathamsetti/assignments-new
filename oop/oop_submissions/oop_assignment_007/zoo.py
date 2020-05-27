class Deer:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        if self._age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(self.age_in_months))
        self._age_in_months=age_in_months
        if self._required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
      
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=2
        
    @classmethod
    def make_sound(cls):
        print("Buck Buck")
        
    @classmethod    
    def breathe(cls):
        print("Breathe in air")
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    
        
class Lion(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=4
        
        
            
    def hunt(self,animal):
        count=0
        for i in animal.animallist:
            if i.__class__== Deer:
                count+=1
                animal.all_animals.remove(i)
                return animal.animallist.remove(i)
        if count==0:
            print("No deers to hunt")
            
                
        
    @classmethod    
    def make_sound(cls):
        print("Roar Roar")
        
        
class Shark(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=8
        
    def hunt(self,animal):
        count=0
        for i in animal.animallist:
            if i.__class__==GoldFish:
                count+=1
                animal.all_animals.remove(i)
                return animal.animallist.remove(i)
        if count==0:
            print("No GoldFish to hunt")
            
    @classmethod    
    def make_sound(cls):
        print("Shark Sound")
    @classmethod    
    def breathe(cls):
        print("Breathe oxygen from water")
        
class GoldFish(Shark):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.2
        
    @classmethod    
    def make_sound(cls):
        print("Hum Hum")
    
class Zoo:
    
    all_animals=[]
    
    def __init__(self):
        self.animallist=[]
        self._reserved_food_in_kgs=0
        

        
        
    def add_food_to_reserve(self,foodkg):
        self._reserved_food_in_kgs+=foodkg
        print(self._reserved_food_in_kgs)
         
        
        
    def add_animal(self,gold_fish):
        self.animallist.append(gold_fish)
        self.all_animals.append(gold_fish)
        
    def count_animals(self):
        return len(self.animallist)
        
            
    def feed(self,gold_fish):
        if self._reserved_food_in_kgs>0:
            self._reserved_food_in_kgs=self._reserved_food_in_kgs-gold_fish._required_food_in_kgs
            gold_fish.grow()
            
    @classmethod      
    def count_animals_in_all_zoos(cls):
        return len(cls.all_animals)


    @staticmethod   
    def count_animals_in_given_zoos(given_zoo):
        c=0
        for i in given_zoo:
            c=c+len(i.animallist)
        return c

    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
            
        
class Snake(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.5
        
    def hunt(self,animal):
        count=0
        for i in animal.animallist:
            if i.__class__== Deer:
                count+=1
                animal.all_animals.remove(i)
                return animal.animallist.remove(i)
        if count==0:
            print("No deers to hunt")

            
    @classmethod
    def make_sound(cls):
        print("Hiss Hiss")
        
'''zoo= Zoo()
nehru_zoological_park = Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
zoo.add_animal(lion)
deer = Deer(age_in_months=1, breed="African Lion", required_food_in_kgs=10)
zoo.add_animal(deer)
nehru_zoological_park.add_animal(lion)
print(Zoo.count_animals_in_given_zoos([]))
print(Zoo.count_animals_in_all_zoos())'''
