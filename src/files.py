"""
This file provide the function called to created the files and folders.

Defines the functions required to create file and folders depending on project type.
"""

import os
import sys

def create_base_files(project_name):
    print("Creating base files...")
    os.system("touch " + project_name + "/README.md")
    print("README.md created")
    os.system("touch " + project_name + "/requirements.txt")
    print("requirements.txt created")
    os.system("touch " + project_name + "/.gitignore")
    print(".gitignore created")
    os.system("touch " + project_name + "/LICENSE")
    print("LICENSE created")
    print("Base files created")

def create_base_folders(project_name):
    print("Creating base folders...")
    os.system("mkdir " + project_name + "/src")
    print("src folder created")
    os.system("mkdir " + project_name + "/tests")
    print("tests folder created")
    print("Base folders created")

def create_lib_files(project_name):
    print("Creating lib files...")
    os.system("touch " + project_name + "/src/__init__.py")
    print("__init__.py created")
    os.system("touch " + project_name + "/src/" + project_name + ".py")
    print(project_name + ".py created")
    print("Lib files created")

def create_app_files(project_name):
    print("Creating app files...")
    os.system("touch " + project_name + "/src/main.py")
    print("main.py created")
    print("App files created")

