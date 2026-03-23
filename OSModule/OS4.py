# By Claude AI

# Directory Operations

"""
2. Directory Operations
Theory:
These functions let you create, delete, rename, and list directories (folders) on your file system. Python sends these commands directly to the OS.

  Function            Description
os.mkdir(path)       Creates a single new directory
os.makedirs(path)    Creates nested directories (parents too)
os.rmdir(path)       Removes an empty directory
os.removedirs(path)  Removes nested empty directories
os.listdir(path)     Returns a list of all entries in the directory
os.rename(src, dst)  Renames a file or directory

"""

import os

#os.mkdir('notes') # Creates single folder
os.makedirs('project/src/utils', exist_ok=True) # Creates full nested path

os.rmdir('notes') # Deletes empty folder
os.removedirs('project/src') # Delets chain if all empty

print(os.listdir('.')) # ['main.py], 'notes', 'data']
