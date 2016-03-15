%pylab inline
from IPython.core.display import display_markdown
import shutil

## TODO: This document will have all global functions like attendance,
## ask, etc.

def attendance(my_name):
    """Saves student's name to the attendance directory.
    
    Saves an extensionless file to avoid concurrency issues with a single
    attendance sheet file.
    """
    
    f=open("/home/main/logs/attendance/"+my_name, "w")
    f.close()
    
def ask(my_question):
    """Submits a question for GMs
    """
    ## TODO
    pass

def get_help():
    """Pings one of the GMs with name and timestamp for help
    """
    ## TODO
    pass

