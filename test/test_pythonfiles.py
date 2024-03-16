import pytest

from pyproject_init.utils import pythonfiles as pyfiles


class TestPythonFiles:
    def test_create_lib(self, tmp_path):
        pyfiles.create_lib(str(tmp_path))
        assert (tmp_path / "src").is_dir()
        assert (tmp_path / "tests").is_dir()
        assert (tmp_path / "docs").is_dir()
        assert (tmp_path / "src" / "__init__.py").is_file()
        assert not (tmp_path / "tests" / "__init__.py").is_file()
        assert not (tmp_path / "docs" / "__init__.py").is_file()

    def test_create_app(self, tmp_path):
        pyfiles.create_app(str(tmp_path))
        assert (tmp_path / "app").is_dir()
        assert (tmp_path / "tests").is_dir()
        assert (tmp_path / "docs").is_dir()
        assert (tmp_path / "app" / "__init__.py").is_file()
        assert not (tmp_path / "tests" / "__init__.py").is_file()
        assert not (tmp_path / "docs" / "__init__.py").is_file()
