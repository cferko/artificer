#%pylab inline
from IPython.core.display import display_markdown
import os, time
import pandas as pd

## TODO: This document will have all global functions like attendance,
## ask, etc.

name_frame = pd.read_csv("../logs/name_map.csv")
name_dict = name_frame.set_index("character name")["student name"].to_dict()

def parse_attendance():
    """Returns dataframe of students attending
    """
    my_path = "../logs/attendance/"
    char_list = os.listdir(my_path)
    time_list = [time.ctime(os.path.getctime(my_path+name)) for name in char_list]
    real_name_list = [name_dict.get(name, 0) for name in char_list]
    
    my_frame = pd.DataFrame(data={'Student':real_name_list, 'Character':
        char_list, 'Time Registered':time_list}).set_index("Character")
        
    return my_frame
    
def poll_questions():
    """Looks for new questions
    """
    

def get_help():
    """Pings one of the GMs with name and timestamp for help
    """
    ## TODO
    pass

