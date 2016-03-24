"""
Base class for all encounters
"""

class BaseEncounter():
    
    def __init__(self,
                 encounter_name,
                 variable_name,
                 scorer_func,
                 failure_output,
                 success_output):
                     
        self.encounter_name = encounter_name
        self.variable_name = variable_name
        self.scorer_func = scorer_func
        self.failure_output = failure_output
        self.success_output = success_output
        
    def __str__(self):
        return self.encounter_name    