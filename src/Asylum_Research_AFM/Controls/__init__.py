import os
import importlib


# Get the current directory (where this __init__.py file is located)

current_directory = os.path.dirname(__file__)

 

# List all the files in this directory

files = os.listdir(current_directory)

 

# Iterate through the files, importing the Python files

for file in files:

    if file.endswith('.py') and file != '__init__.py':

        module_name = file[:-3] # Removing the .py extension

        # Dynamically import the module using importlib

        module = importlib.import_module(f'.{module_name}', package=__package__)
