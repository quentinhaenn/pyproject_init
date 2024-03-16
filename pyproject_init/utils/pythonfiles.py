"""
This file provide the functions to create the python files, including the __init__.py file.
"""

import os

TRAD_DIRS = ["tests", "docs"]
LIB_DIRS = ["src"] + TRAD_DIRS
APP_DIRS = ["app"] + TRAD_DIRS


def create_lib(project_path):
    """
    Create the files and dirs for a library project
    """
    _create_dirs(project_path, LIB_DIRS)
    _create_init_files(project_path, LIB_DIRS)


def create_app(project_path):
    """
    Create the files and dirs for an application project
    """
    _create_dirs(project_path, APP_DIRS)
    _create_init_files(project_path, APP_DIRS)


def _create_dirs(project_path, dirs):
    """
    Create the directories
    """
    for directory in dirs:
        os.makedirs(os.path.join(project_path, directory))


def _create_init_files(project_path, dirs):
    """
    Create the __init__.py files
    """
    for directory in dirs:
        if directory not in TRAD_DIRS:
            with open(os.path.join(project_path, directory, "__init__.py"), "w") as init_file:
                pass
