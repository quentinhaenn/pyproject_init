import pytest
import os

from pyproject_init.utils import projectfiles as pfiles


class TestProjectFiles:
    def test_create_readme(self, tmp_path):
        pfiles._create_readme(str(tmp_path))
        readme_path = os.path.join(tmp_path, "README.md")
        assert os.path.isfile(readme_path)
        with open(readme_path, "r") as readme:
            content = readme.read()
            assert content.startswith("# " + str(tmp_path))
            assert "This is the README file for the " + str(tmp_path) + " project." in content
            assert "You can write here a description of your project." in content
            assert "Suggested sections:" in content
            assert "- Presentation" in content
            assert "- Installation" in content
            assert "- Usage" in content
            assert "- Contributing" in content
            assert "- License" in content

    def test_create_gitignore(self, tmp_path):
        pfiles._create_gitignore(str(tmp_path))
        gitignore_path = os.path.join(str(tmp_path), ".gitignore")
        assert os.path.isfile(gitignore_path)
        with open(gitignore_path, "r") as gitignore:
            content = gitignore.read()
            assert "# Configuration files\n" in content
            assert ".vscode/\n" in content
            assert ".DS_Store\n" in content
            assert "# pytest artifacts\n" in content
            assert "*.pyc\n" in content
            assert "__pycache__/\n" in content
            assert "# Coverage\n" in content
            assert "htmlcov/\n" in content
            assert ".coverage\n" in content
            assert ".pytest_cache/\n" in content
            assert "# Distribution\n" in content
            assert "build/\n" in content
            assert "dist/\n" in content
            assert ".eggs/\n" in content
            assert "# Documentation source build\n" in content
            assert "doc/_build\n" in content

    def test_create_license(self, tmp_path):
        pfiles._create_license(str(tmp_path), "MIT")
        license_path = os.path.join(tmp_path, "LICENSE")
        assert os.path.isfile(license_path)
        with open(license_path, "r") as license:
            content = license.read()
            assert "MIT License" in content
            assert "Permission is hereby granted, free of charge, to any person obtaining a copy" in content
            assert 'of this software and associated documentation files (the "Software"), to deal' in content

    def test_create_setupcfg(self, tmp_path):
        pfiles._create_setupcfg(str(tmp_path), "MIT")
        setupcfg_path = os.path.join(tmp_path, "setup.cfg")
        assert os.path.isfile(setupcfg_path)
        with open(setupcfg_path, "r") as setupcfg:
            content = setupcfg.read()
            assert "[metadata]\n" in content
            assert "name = " in content
            assert "version = 0.1.0\n" in content
            assert "author = " in content
            assert "author_email = " in content
            assert "description = " in content
            assert "long_description = file: README.md\n" in content
            assert "long_description_content_type = text/markdown\n" in content
            assert "url = " in content
            assert "license = MIT\n" in content

    def test_create_setuppy(self, tmp_path):
        pfiles._create_setuppy(str(tmp_path), "MIT")
        setuppy_path = os.path.join(tmp_path, "setup.py")
        assert os.path.isfile(setuppy_path)
        with open(setuppy_path, "r") as setuppy:
            content = setuppy.read()
            assert "import setuptools\n" in content
            assert 'with open("README.md", "r") as fh:\n' in content
            assert "long_description = fh.read()\n" in content
            assert "setup(\n" in content
            assert "name=" in content
            assert "version=" in content
            assert "author=" in content
            assert "author_email=" in content
            assert "description=" in content
            assert "long_description=long_description,\n" in content
            assert "url=" in content

    def test_create_pyproject(self, tmp_path):
        pfiles._create_pyproject(str(tmp_path))
        pyproject_path = os.path.join(tmp_path, "pyproject.toml")
        assert os.path.isfile(pyproject_path)
        with open(pyproject_path, "r") as pyproject:
            content = pyproject.read()
            assert "[build-system]\n" in content
            assert 'requires = ["setuptools", "wheel"]\n' in content
            assert 'build-backend = "setuptools.build_meta"\n' in content

    def test_create_base_files(self, tmp_path):
        pfiles.create_base_files(str(tmp_path), "MIT", True, True, True)
        assert os.path.isfile(os.path.join(tmp_path, "README.md"))
        assert os.path.isfile(os.path.join(tmp_path, ".gitignore"))
        assert os.path.isfile(os.path.join(tmp_path, "LICENSE"))
        assert os.path.isfile(os.path.join(tmp_path, "setup.cfg"))
        assert os.path.isfile(os.path.join(tmp_path, "setup.py"))
        assert os.path.isfile(os.path.join(tmp_path, "pyproject.toml"))
