"""
Test file for cli.py
"""

import pytest
import os

from click.testing import CliRunner
from pyproject_init.cli import lib, app


class TestCli:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_lib(self, runner, tmp_path):
        os.chdir(tmp_path)
        result = runner.invoke(
            lib,
            [
                "--setuppy",
                "--setupcfg",
                "--pyproject",
                "--git",
                "--virtualenv",
                "--docker",
                "--license",
                "MIT",
                "test_project",
            ],
        )
        print(result.output)
        assert result.exit_code == 0
        assert os.path.isdir(os.path.join(tmp_path, "test_project"))
        assert os.path.isfile(os.path.join(tmp_path, "setup.py"))
        assert os.path.isfile(os.path.join(tmp_path, "setup.cfg"))
        assert os.path.isfile(os.path.join(tmp_path, "pyproject.toml"))
        assert os.path.isdir(os.path.join(tmp_path, "test_project-env"))
        assert os.path.isfile(os.path.join(tmp_path, "Dockerfile"))
        assert os.path.isdir(os.path.join(tmp_path, ".git"))
        assert os.path.isfile(os.path.join(tmp_path, "LICENSE"))
        assert os.path.isfile(os.path.join(tmp_path, "README.md"))

    def test_app(self, runner, tmp_path):
        os.chdir(tmp_path)
        result = runner.invoke(
            app,
            [
                "test_project",
                "--setuppy",
                "--setupcfg",
                "--pyproject",
                "--git",
                "--virtualenv",
                "--docker",
                "--license",
                "MIT",
            ],
        )
        assert result.exit_code == 0
        assert os.path.isdir(os.path.join(tmp_path, "test_project"))
        assert os.path.isfile(os.path.join(tmp_path, "setup.py"))
        assert os.path.isfile(os.path.join(tmp_path, "setup.cfg"))
        assert os.path.isfile(os.path.join(tmp_path, "pyproject.toml"))
        assert os.path.isdir(os.path.join(tmp_path, "test_project-env"))
        assert os.path.isfile(os.path.join(tmp_path, "Dockerfile"))
        assert os.path.isdir(os.path.join(tmp_path, ".git"))
        assert os.path.isfile(os.path.join(tmp_path, "LICENSE"))
        assert os.path.isfile(os.path.join(tmp_path, "README.md"))
