c = get_config()
c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.exec_files = [
    'notebook_setup.py'
]