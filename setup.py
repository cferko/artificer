import shutil, subprocess
subprocess.call("ipython profile create", kernel=True)
shutil.copy("/home/main/notebooks/code/ipython_config.py", 
            "/home/main/.ipython/profile_default/ipython_config.py")
shutil.copy("/home/main/notebooks/code/ipython_magics.py",
            "/home/main/.ipython/startup/ipython_magics.py")