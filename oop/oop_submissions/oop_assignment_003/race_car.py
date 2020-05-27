import math
from car import Car
class RaceCar(Car):
    horn="Peep Peep\nBeep Beep"
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
       
    def accelerate(self): 
        if self._nitro>=10:
            self._nitro=self._nitro-10
            self._current_speed=self._current_speed+math.ceil(self._acceleration*0.3)
        super().accelerate()
        
    def apply_brakes(self):
        if self._current_speed>self._max_speed/2:
            self._nitro+=10
        super().apply_brakes()
        
    @property
    def nitro(self):
        return self._nitro
        
    
       
       
    
        
    