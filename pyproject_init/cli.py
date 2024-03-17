"""
This file provide the cli interface for the pyproject initializer.
"""

from __future__ import absolute_import
import os

from click import echo
import click

from pyproject_init import __version__
from pyproject_init.pyproject_initializer import PyprojectInitializer


@click.group(context_settings={"help_option_names": ("-h", "--help")})
@click.version_option(__version__, "-V", "--version", message="%(version)s")
def cli():
    """
    Pyproject initializer
    """


# Commands available :
# - lib : create a library project
# - app : create an application project

# Options available :
# - setuppy : create a setup.py file
# - setupcfg : create a setup.cfg file
# - pyproject : create a pyproject.toml file
# - git : initialize a git repository
# - virtualenv : create a virtualenv
# - docker : create a docker file
# - license : choose the license type
# - project_name : name of the project
# - project_type : type of the project (lib or app)


@cli.command()
@click.option(
    "--setup", is_flag=True, help="If set, create a setup.py and a setup.cfg file, if not creates pyproject.toml"
)
@click.option("--git", is_flag=True, help="Initialize a git repository")
@click.option("--virtualenv", is_flag=True, help="Create a virtualenv")
@click.option("--docker", is_flag=True, help="Create a docker file")
@click.option("--license", "license_name", default="MIT", help="Choose the license type")
@click.argument("project_name", required=True)
def lib(setup, git, virtualenv, docker, license_name, project_name):
    """
    Create a library project
    """
    echo("Creating a library project")
    project_root = os.getcwd()
    initializer = PyprojectInitializer(project_name, project_root, "lib", setup, git, virtualenv, docker, license_name)
    initializer.init()
    echo("Library project created")


@cli.command()
@click.option(
    "--setup", is_flag=True, help="If set, create a setup.py and a setup.cfg file, if not creates pyproject.toml"
)
@click.option("--git", is_flag=True, help="Initialize a git repository")
@click.option("--virtualenv", is_flag=True, help="Create a virtualenv")
@click.option("--docker", is_flag=True, help="Create a docker file")
@click.option("--license","license_name", default="MIT", help="Choose the license type")
@click.argument("project_name", required=True)
def app(setup, git, virtualenv, docker, license_name, project_name):
    """
    Create an application project
    """
    echo("Creating an application project")
    project_root = os.getcwd()
    initializer = PyprojectInitializer(project_name, project_root, "app", setup, git, virtualenv, docker, license_name)
    initializer.init()
    echo("Application project created")


if __name__ == "__main__":
    cli()
