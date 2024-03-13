"""
This file define function to create annex files and dir.
"""

import os
import sys

def init_virtualenv(venv_name = "venv"):
    """
    init_virtualenv initialize a virtual environment for project
    """
    print("Creating virtual environment")
    os.system("python3 -m venv " + venv_name)
    print("Virtual environment created")

def init_git(project_name):
    """
    init_git initialize a git repository for the project
    """
    print("Initializing git repository")
    os.system("git init " + project_name)
    print("Git repository initialized")

def create_base_files(project_name):
    