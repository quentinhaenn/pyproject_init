"""
This file provide the main class for the pyproject initializer.
"""

import os
import subprocess

from pyproject_init.utils import projectfiles as files, pythonfiles as pyfiles


class PyprojectInitializer:
    """
    This class provides the main functionality for the pyproject initializer.

    Args:

        project_name (str): The name of the project
        project_root (str): The root directory of the project
        project_type (str): The type of the project (lib or app)
        setup (bool): If True, create a setup.py file
        git_needed (bool): If True, initialize a git repository
        virtualenv_needed (bool): If True, initialize a virtual environment
        docker_needed (bool): If True, create a Dockerfile
        license_name (str): The name of the license to use
    """

    def __init__(
        self,
        project_name,
        project_root,
        project_type,
        setup=False,
        git_needed=False,
        virtualenv_needed=False,
        docker_needed=False,
        license_name="MIT",
    ):
        self.project_name = project_name
        self.project_root = project_root
        self.project_path = os.path.join(self.project_root, self.project_name)
        self.project_type = project_type
        self.setup = setup
        self.git = git_needed
        self.virtualenv = virtualenv_needed
        self.docker = docker_needed
        self.license_name = license_name

    def init(self):
        """
        Initialize the project
        """
        files.create_base_files(self.project_root, self.license_name, self.setup)
        if self.project_type == "lib":
            self.create_lib_project()
        elif self.project_type == "app":
            self.create_app_project()

        if self.git:
            self.init_git()
            files.create_gitignore(self.project_root, self.project_name)

        if self.virtualenv:
            self.init_virtualenv()

        if self.docker:
            self.init_docker()

    def create_lib_project(self):
        """
        Create a library project
        """
        pyfiles.create_lib(self.project_path)

    def create_app_project(self):
        """
        Create an application project
        """
        pyfiles.create_app(self.project_path)

    def init_git(self):
        """
        Initialize the git repository
        """
        subprocess.run(["git", "init"], cwd=self.project_root, check=True)

    def init_virtualenv(self):
        """
        Initialize the virtual environment
        """
        subprocess.run(["python3", "-m", "venv", self.project_name + "-env"], cwd=self.project_root, check=True)

    def init_docker(self):
        """
        Create a base Dockerfile
        """
        with open(os.path.join(self.project_root, "Dockerfile"), "w", encoding="utf-8") as dockerfile:
            dockerfile.write("# This is an example Dockerfile. Modify it to match your needs\n")
            dockerfile.write("# Use the official image as a parent image\n")
            dockerfile.write("FROM <image name>\n")
            dockerfile.write("ADD . /<container directory>\n")
            dockerfile.write("WORKDIR /<container directory>\n")
            dockerfile.write("# Install the dependencies\n")
            dockerfile.write("RUN pip install -r requirements.txt\n")
            dockerfile.write("# Run the application\n")
            dockerfile.write("CMD python app.py\n")
