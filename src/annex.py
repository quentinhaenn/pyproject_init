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

def init_docker():
    """
    init_docker initialize a docker environment for the project
    """
    print("Creating Dockerfile")
    os.system("touch Dockerfile")
    print("Dockerfile created")

def writing_license(license, project_name):
    """
    writing_license write the license in the LICENSE file
    """
    