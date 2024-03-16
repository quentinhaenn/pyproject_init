"""
This module contains the functions to create the project files.
"""

import os
import requests


def create_base_files(
    project_path, license_type="MIT", setupcfg_needed=False, setuppy_needed=False, pyproject_needed=False
):
    """
    Create the base files for a project.

    This function creates the following base files:
    - README.md
    - .gitignore
    - LICENSE
    - pyproject.toml (optional)
    - setup.cfg (optional)
    - setup.py (optional)

    The files are created in the project_path directory.
    The optional files are created depending on user's choice.
    """

    _create_readme(project_path)
    _create_gitignore(project_path)
    _create_license(project_path, license_type)
    if setupcfg_needed:
        _create_setupcfg(project_path, license_type)
    if setuppy_needed:
        _create_setuppy(project_path, license_type)
    if pyproject_needed:
        _create_pyproject(project_path)


def _create_readme(project_path):
    """
    Create the README.md file
    """
    with open(os.path.join(project_path, "README.md"), "w") as readme:
        readme.write("# " + project_path + "\n")
        readme.write("This is the README file for the " + project_path + " project.\n")
        readme.write("You can write here a description of your project.\n")
        readme.write("Suggested sections:\n")
        readme.write("- Presentation\n")
        readme.write("- Installation\n")
        readme.write("- Usage\n")
        readme.write("- Contributing\n")
        readme.write("- License\n")


def _create_gitignore(project_path):
    """
    _create_gitignore creates the .gitignore file

    Args:
        project_path (str): path to the project root directory
    """
    with open(os.path.join(project_path, ".gitignore"), "w") as gitignore:
        gitignore.write("# Configuration files\n")
        gitignore.write(".vscode/\n")
        gitignore.write(".DS_Store\n")
        gitignore.write("\n")
        gitignore.write("# pytest artifacts\n")
        gitignore.write("*.pyc\n")
        gitignore.write("__pycache__/\n")
        gitignore.write("\n")
        gitignore.write("# Coverage\n")
        gitignore.write("htmlcov/\n")
        gitignore.write(".coverage\n")
        gitignore.write(".pytest_cache/\n")
        gitignore.write("\n")
        gitignore.write("# Distribution\n")
        gitignore.write("build/\n")
        gitignore.write("dist/\n")
        gitignore.write(".eggs/\n")
        gitignore.write("\n")
        gitignore.write("# Documentation source build\n")
        gitignore.write("doc/_build\n")


def _create_license(project_path, license_type="MIT"):
    """
    Create the LICENSE file
    """
    licence_url = f"https://api.github.com/licenses/" + license_type.lower()
    try:
        licence = requests.get(licence_url).json()
        with open(os.path.join(project_path, "LICENSE"), "w") as license_file:
            license_file.write(licence["body"])
    except requests.exceptions.RequestException as e:
        print("An error occured while trying to get license from GitHub API")
        print(e)


def _create_setupcfg(project_path, license_type="MIT"):
    """
    Create the setup.cfg file
    """
    with open(os.path.join(project_path, "setup.cfg"), "w") as setupcfg:
        setupcfg.write("[metadata]\n")
        setupcfg.write("name = " + project_path + "\n")
        setupcfg.write("version = 0.1.0\n")
        setupcfg.write("author = Your Name\n")
        setupcfg.write("author_email = youremail@some.com\n")
        setupcfg.write("description = A short description of the project\n")
        setupcfg.write("long_description = file: README.md\n")
        setupcfg.write("long_description_content_type = text/markdown\n")
        setupcfg.write("url = url to the project\n")
        setupcfg.write("license = {}\n".format(license_type))
        setupcfg.write("\n")
        setupcfg.write("[flake8]\n")
        setupcfg.write("max-line-length = 120\n")
        setupcfg.write("exclude = .git,__pycache__,docs/source/conf.py,old,build,dist\n")


def _create_setuppy(project_path, license_type="MIT"):
    """
    Create the setup.py file
    """
    with open(os.path.join(project_path, "setup.py"), "w") as setuppy:
        setuppy.write("import setuptools\n")
        setuppy.write("\n")
        setuppy.write('with open("README.md", "r") as fh:\n')
        setuppy.write("    long_description = fh.read()\n")
        setuppy.write("\n")
        setuppy.write("setuptools.setup(\n")
        setuppy.write('    name="' + project_path + '",\n')
        setuppy.write('    version="0.0.1",\n')
        setuppy.write('    author="Your Name",\n')
        setuppy.write('    author_email="your email",\n')
        setuppy.write('    description="A short description of the project",\n')
        setuppy.write("    long_description=long_description,\n")
        setuppy.write('    url="url to the project",\n')
        setuppy.write('    license="{}",\n'.format(license_type))
        setuppy.write("    install_requires=[put your requirements here],\n")
        setuppy.write('    packages=["put your packages here"],\n')
        setuppy.write('    keywords=["put your keywords here"],\n')
        setuppy.write("    classifiers=[\n")
        setuppy.write("        Put your classifiers here,\n")
        setuppy.write("    ],\n")
        setuppy.write("    include_package_data=True,\n")
        setuppy.write(")\n")


def _create_pyproject(project_path):
    """
    Create the pyproject.toml file
    """
    with open(os.path.join(project_path, "pyproject.toml"), "w") as pyproject:
        pyproject.write("[build-system]\n")
        pyproject.write('requires = ["setuptools", "wheel"]\n')
        pyproject.write('build-backend = "setuptools.build_meta"\n')
