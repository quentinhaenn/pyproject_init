"""
This file provide the main class for the pyproject initializer.
"""

import os
import sys

import src.files as files
import src.annex as annex

class PyprojectInitializer:

    def __init__(self, project_name, project_type, git_needed = False, virtualenv_needed = False, docker_needed = False,license = "MIT"):
        self.project_name = project_name
        self.project_type = project_type
        self.git = git_needed
        self.virtualenv = virtualenv_needed
        self.docker = docker_needed
        self.license = license

    def init(self):
        """
        Initialize the project
        """
        files.create_base_files(self.project_name)
        files.create_base_folders(self.project_name)
        if self.project_type == "lib":
            self.create_lib_project()
        elif self.project_type == "app":
            self.create_app_project()
        
        if self.git :
            self.init_git()
        
        if self.virtualenv:
            self.init_virtualenv()
        
        if self.docker:
            self.init_docker()


    def create_lib_project(self):
        """
        Create a library project
        """
        files.create_lib_files(self.project_name)
    
    def create_app_project(self):
        """
        Create an application project
        """
        files.create_app_files(self.project_name)

    def init_git(self):
        """
        Initialize git
        """
        annex.init_git(self.project_name)
    
    def init_virtualenv(self):
        """
        Initialize virtualenv
        """
        annex.init_virtualenv(self.project_name)
    
    def init_docker(self):
        """
        Initialize docker
        """
        annex.init_docker(self.project_name)
    
    def __str__(self):
        return f"PyprojectInitializer(project_name={self.project_name}, project_type={self.project_type}, git_needed={self.git}, virtualenv_needed={self.virtualenv}, docker_needed={self.docker}, license={self.license})"
    
    def __repr__(self):
        return f"PyprojectInitializer(project_name={self.project_name}, project_type={self.project_type}, git_needed={self.git}, virtualenv_needed={self.virtualenv}, docker_needed={self.docker}, license={self.license})"
