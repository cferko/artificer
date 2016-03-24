"""
A simple test encounter
"""
from .base import BaseEncounter

class LevelOne(BaseEncounter):

    def score(self):
        try:
            variable = eval(self.variable_name)
            
        except:
            print "You haven't defined test."
            return -1
            
        if variable == 5:
            return 1
        else:
            return -1
            
    def __init__(self):
        self.encounter_name = "level_1"
        self.variable_name = "test"
        self.success_output = "Good, test equals 5."
        self.failure_output = "You didn't set test equal to 5."
        self.undefined_output = "You haven't defined test."
        
class LevelTwo(BaseEncounter):

    def score(self):
        try:
            variable = eval(self.variable_name)
            
        except:
            print "You haven't defined derp."
            return -1
            
        if variable == 5:
            return 1
        else:
            return -1
            
            
    def __init__(self):
        self.encounter_name = "level_2"
        self.variable_name = "derp"
        self.success_output = "Good, derp equals 5."
        self.failure_output = "You didn't set derp equal to 5."
        self.undefined_output = "You haven't defined derp."
        
        
class LevelThree(BaseEncounter):

    def score(self):
        try:
            variable = eval(self.variable_name)
            
        except:
            print "You haven't defined herp."
            return -1
            
        if variable == 5:
            return 1
        else:
            return -1
            
            
    def __init__(self):
        self.encounter_name = "level_3"
        self.variable_name = "herp"
        self.success_output = "Good, herp equals 5."
        self.failure_output = "You didn't set herp equal to 5."
        self.undefined_output = "You haven't defined herp."
        

def get_encounter(name):
    if name=="test":
        return LevelOne()
    elif name=="derp":
        return LevelTwo()
    elif name=="herp":
        return LevelThree()