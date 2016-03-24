import sys
sys.path.insert(0, "..")
import encounters

## This is basically pseudocode at this point -- still todo

def scorer1(fn):
    if fn(1)==1:
        return 1, "good"
    else:
        return 0, "okay"
        
def scorer2(fn):
    return (fn() == True), ""

def handle_transition(arg):
    return None

scorer_dict = {'func_1' : scorer1, 'func_2':scorer2}

def update_state(self, old_state, namespace_variables):
    current_state = old_state.copy()

    current_level = current_state["level"]
    active = current_state["target_variables"]
    completed = current_state["completed_variables"]        
    current_score = current_state["score"]        
    
    for varname in active:
        if varname not in namespace_variables:
            print varname, "has not been completed!"
        elif varname in namespace_variables:
            var=eval(varname)
            this_scorer = scorer_dict[varname]
            my_score, my_output = this_scorer(var)
            if my_score == -1:
                print varname, "did not behave as expected; please try again."
            elif my_score >= 0:
                completed.append(varname)
                active.remove(varname)
                print my_output
                current_score += my_score
    
    current_state["score"] = current_score
    current_state["active"] = active
    current_state["completed"] = completed
    
    transition = handle_transition(current_state)
    
    if transition != None:
        display_transition(transition)
        
    return current_state
    
current_state={'level':0, 'target_variables':['func_1', 'func_2'], 
               'completed_variables':[], 'score':0}
pickle.dump(current_state, open("state.p", "wb"))