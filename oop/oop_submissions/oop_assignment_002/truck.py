from car import Car
class Truck(Car):
    horn="Honk Honk"
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        if max_cargo_weight>0:
            self._max_cargo_weight= max_cargo_weight
        else:
            raise ValueError("Invalid value for cargo_weight")
        self._loads=0
      
            
    def load(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError("Invalid value for cargo_weight")
        if (self._is_engine_started==True or self._is_engine_started==False) and self._current_speed==0 and self._loads+cargo_weight<=self._max_cargo_weight:
            self._loads+=cargo_weight
        elif self._loads+cargo_weight >self._max_cargo_weight:
            print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        else:
            print("Cannot load cargo during motion")
             
            
    def unload(self,cargo_weight):
        if self._is_engine_started==True and self._current_speed==0:
            self._loads-= cargo_weight
        elif self._is_engine_started==True and self._current_speed!=0:
            print("Cannot unload cargo during motion")
        
        elif cargo_weight<0:
            raise ValueError("Invalid value for cargo_weight")
        else:
            self._loads-= cargo_weight
            
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
            
            
            
            

