c = get_config()
c.TerminalIPythonApp.display_banner = False
c.InteractiveShellApp.exec_files = [
    'notebook_setup.py'
]