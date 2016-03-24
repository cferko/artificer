import shutil, subprocess, os

subprocess.call("ipython profile create", shell=True)
shutil.copy("/home/main/notebooks/code/ipython_config.py", 
            "/home/main/.ipython/profile_default/ipython_config.py")
shutil.copy("/home/main/notebooks/code/ipython_magics.py",
            "/home/main/.ipython/profile_default/startup/ipython_magics.py")