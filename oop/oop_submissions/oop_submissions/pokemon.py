class Pokemon:
    sound=''
    swimming=''
    def __init__(self,name,level):
        self._name=name
        self._level=level
        if self._name=="":
            raise ValueError("name cannot be empty")
        if self._level<=0:
            raise ValueError("level should be > 0")
        self._master= "No Master"
            
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
    @property
    def master(self):
        if self._master== "No Master":
            print("No Master")
        else:
            return self._master
            
    @classmethod        
    def make_sound(cls):
        print(cls.sound)
    

    @classmethod
    def swim(cls):
        print(cls.swimming)
        
    def __str__(self):
        return "{} - Level {}".format(self.name,self.level)
        
class runninganimal:
    def run(self):
        running="Pikachu running..."
    
class Pikachu(Pokemon,runninganimal):
    sound="Pika Pika"
    def run(self):
        super().run()
    def attack(self):
        print("Electric attack with {} damage".format(self.level*10))
        
    
class Squirtle(Pokemon): 
    sound="Squirtle...Squirtle"
    running="Squirtle running..."
    swimming="Squirtle swimming..."

    def attack(self):
        print("Water attack with {} damage".format(self.level*9))
        

class Pidgey(Pokemon):
    sound="Pidgey...Pidgey"
    flying="Pidgey flying..."
    
    def attack(self):
        print("Air attack with {} damage".format(self.level*5))
    
class Swanna(Pokemon):
    sound="Swanna...Swanna"
    flying="Swanna flying..."
    swimming="Swanna swimming..."

    def attack(self):
        print("Water attack with {} damage".format(self.level*9))
        print("Air attack with {} damage".format(self.level*5))
        

class Zapdos(Pokemon):
    sound="Zap...Zap"
    flying="Zapdos flying..."

    def attack(self):
        print("Electric attack with {} damage".format(self.level*10))
        print("Air attack with {} damage".format(self.level*5))

class Island:
    
    total_islands=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.total_islands.append(self)

    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
   
    def add_pokemon(self,poke):
        self._pokemon_left_to_catch+=1
        if self._pokemon_left_to_catch>self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
            self._pokemon_left_to_catch=self._max_no_of_pokemon
          
    @classmethod
    def get_all_islands(cls):
        return cls.total_islands
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)

class Trainer(Island):
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self.experience
        self._food_in_bag=0
        self._current_island=None
        self.catch_list=[]
    
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    @property
    def current_island(self):
        if self._current_island==None:
            print("You are not on any island")
        else:
            return self._current_island
        
    def __str__(self):
        return "{}".format(self.name)
    
    
    def move_to_island(self,island):
        self._current_island=island

    def collect_food(self):
        if self._current_island==None or self.current_island._total_food_available_in_kgs==0:
            print("Move to an island to collect food")
        elif self.current_island._total_food_available_in_kgs<self._max_food_in_bag:
            self._food_in_bag=self.current_island._total_food_available_in_kgs
            self.current_island._total_food_available_in_kgs=0
        elif self._food_in_bag==self._max_food_in_bag:
            self._food_in_bag=self._food_in_bag
            self.current_island._total_food_available_in_kgs=self.current_island._total_food_available_in_kgs
        else:
            self.current_island._total_food_available_in_kgs=self.current_island._total_food_available_in_kgs-self._max_food_in_bag
            self._food_in_bag=self._max_food_in_bag
            
    def catch(self,pokemon_value):
        if self._experience>=100*pokemon_value._level:
            self.catch_list.append(pokemon_value)
            self._experience+=pokemon_value._level*20
            pokemon_value._master=self
            print("You caught {}".format(pokemon_value._name))
        else:
            print("You need more experience to catch {}".format(pokemon_value._name))
            
    def get_my_pokemon(self):
        return self.catch_list


            

    