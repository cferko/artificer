# This code can be put in any Python module, it does not require IPython
# itself to be running already.  It only creates the magics subclass but
# doesn't instantiate it yet.
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
import pickle

import sys
sys.path.insert(0, "/home/main/notebooks/code/")
import update_state

"""
Design idea: checkpoint is a line magic that handles all updating of quest
progression logic. Each time it is called, checkpoint will search through
the local variables for new functions or strings that have been defined,
then scores them and updates state accordingly. Each such checkpoint
will then update the list of functions or strings to look for next time.
"""

@magics_class
class MyMagics(Magics):

    @line_magic
    def checkpoint(self, line):
        """Cell magic to score progress and update state
        """
        current_state = pickle.load(open("state.p", "rb"))
        namespace_variables = self.shell.user_ns.keys()
        
        current_state = update_state.update_state(current_state, namespace_variables)
        transition = update_state.handle_transition(current_state)
        
        if transition != None:
            update_state.display_transition(transition)
        
        pickle.dump(current_state, open("state.p", "wb"))
        return

ip = get_ipython()
ip.register_magics(MyMagics)