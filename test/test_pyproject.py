import pytest
import os
import subprocess

from pyproject_init.pyproject_initializer import PyprojectInitializer


class TestPyprojectInitializer:
    def test_init(self, tmp_path):
        py_test = PyprojectInitializer("test_project", str(tmp_path), "lib", True, True, True, True, True, True, "MIT")
        assert py_test.project_name == "test_project"
        assert py_test.project_root == str(tmp_path)
        assert py_test.project_path == os.path.join(str(tmp_path), "test_project")
        assert py_test.project_type == "lib"
        assert py_test.setuppy is True
        assert py_test.setupcfg is True
        assert py_test.pyproject is True
        assert py_test.git is True
        assert py_test.virtualenv is True
        assert py_test.docker is True
        assert py_test.license is "MIT"

    def test_init_git(self, tmp_path):
        py_test = PyprojectInitializer("test_project", str(tmp_path), "lib", True, True, True, True, True, True, "MIT")
        py_test.init_git()
        assert os.path.isdir(os.path.join(str(tmp_path), ".git"))
        subprocess.run(["rm", "-rf", os.path.join(str(tmp_path), ".git")], check=True)

    def test_init_virtualenv(self, tmp_path):
        py_test = PyprojectInitializer("test_project", str(tmp_path), "lib", True, True, True, True, True, True, "MIT")
        py_test.init_virtualenv()
        assert os.path.isdir(os.path.join(str(tmp_path), "test_project-env"))
        subprocess.run(["rm", "-rf", os.path.join(str(tmp_path), "test_project-env")], check=True)

    def test_init_docker(self, tmp_path):
        py_test = PyprojectInitializer("test_project", str(tmp_path), "lib", True, True, True, True, True, True, "MIT")
        py_test.init_docker()
        assert os.path.isfile(os.path.join(str(tmp_path), "Dockerfile"))
