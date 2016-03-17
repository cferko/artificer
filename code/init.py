#%pylab inline
from IPython.core.display import display_markdown
import shutil, os
from datetime import datetime
import pandas as pd

## TODO: This document will have all global functions like attendance,
## ask, etc.

def attendance(my_name):
    """Saves student's name to the attendance directory.
    
    Saves an extensionless file to avoid concurrency issues with a single
    attendance sheet file.
    """
    ## TODO: this is clunky, should handle by log creation
    f=open("../logs/attendance/"+my_name, "w")
    f.close()
    
def ask(my_question):
    """Submits a question for GMs
    
    Assumed to be run by a student with defined state variables
    """
    my_path = "../logs/ask/"
    questions = os.listdir("../logs/ask/")
    if len(questions)==0:
        my_index='0'
    else:
        my_index = str(1 + max([int(q) for q in questions]))
    
    now = datetime.now().ctime()  ## Different between Windows/Unix
    header="Student Name,Character Name,Email,Time,Question,Seen Yet"
    f=open(my_path+my_index, "w")
    f.write(header+"\n")
    f.write(my_name+','+my_char+','+my_email+','+now+','+my_question+',False')
    f.close()

def get_help():
    """Pings one of the GMs with name and timestamp for help
    """
    ## TODO
    pass

if __name__=="__main__":
    ## This runs every time a student starts a new notebook, so we keep
    ## their name and state variables

    my_index = os.getcwd().split('/')[-1]
    print "Testing index fetch. Index is", my_index
    ## Does this use the directory init is called from, or the one it's in?
    
    dataframe = pd.read_csv("../logs/name_map.csv")
    
## This line is just for testing
    my_index="ao"
    
    my_row = dataframe[dataframe["index"]==my_index]
    my_name = my_row["student name"][0]
    my_char = my_row["character name"][0]
    my_email = my_row["email"][0]
    
    ## Note -- also need to update state of current notebook file. Should
    ## probably fetch this from