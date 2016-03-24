import sys
sys.path.insert(0, "/home/main/notebooks")
import encounters
import shutil
from IPython.core.display import display
import pickle

## This is basically pseudocode at this point -- still todo

from IPython.core.display import HTML

def handle_transition(current_state):
    if len(current_state["completed"])<3:
        return None
    else:
        shutil.copy("/home/main/notebooks/source/cadon/cadon_draft.ipynb", 
                    "./next_level.ipynb")

        my_display = """End of Mission
        
        This is a markdown cell with a summary of your performance.
        
        <a href = "next_level.ipynb" target="_blank">Click here</a> for your next mission."""
        
        display(HTML(my_display))
        
        return True

def update_state(old_state, namespace_variables):
    current_state = old_state.copy()

    current_level = current_state["level"]
    active = current_state["active"]
    completed = current_state["completed"]        
    current_score = current_state["score"]        
    
    for varname in active:
        if varname not in namespace_variables:
            print varname, "has not been completed!"
        elif varname in namespace_variables:
            var=eval(varname)
            
            this_encounter = encounters.test.get_encounter(varname) 
            
            this_score = this_encounter.score()
            if this_score == -1:
                print varname, "did not behave as expected; please try again."
            elif this_score >= 0:
                completed.append(varname)
                active.remove(varname)
                current_score += this_score
    
    current_state["score"] = current_score
    current_state["active"] = active
    current_state["completed"] = completed
    
    transition = handle_transition(current_state)
        
    return current_state

current_state={'level':0, 'active':['test', 'derp', 'herp'], 
               'completed':[], 'score':0}
pickle.dump(current_state, open("state.p", "wb"))