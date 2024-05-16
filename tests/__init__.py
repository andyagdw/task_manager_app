'''Initialise package and set up project environment.

This module initialises the package and sets up the project environment
by:
1. Getting the current working directory.
2. Constructing the path to a directory named "src" within the current
working directory.
3. Modifying the Python module search path to include the "src"
directory.

Attributes:
    PROJECT_PATH (str): The absolute path of the current working
    directory.
    SOURCE_PATH (str): The absolute path of the "src" directory
    within the project.
'''
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)
