# PYPROJECT_INIT, the python project initializer

This is a simple python project initializer. It creates any file and directory structure needed for a python project, depending on the options you provide.

## ROADMAP

- [x] add function for creating the chosen license file
- [x] add function for creating the chosen gitignore file
- [x] add function for creating the chosen README file
- [x] modify each os.system() call to use the subprocess module
- [x] wrap the whole thing in a class
- [x] simplify entry point
- [x] add tests
- [ ] add documentation
- [x] add pyproject.toml file
- [x] wrap the whole thing in a package
- [ ] publish the package on pypi
- [x] add a command line interface
- [ ] test it vanilla

## DESCRIPTION

This package is a simple python project initializer. It creates a directory structure and files for a python project, depending on the options you provide. It can create a directory structure for a simple python project, a python package, or a python package with a CLI. It embeds:

- a license file, default containing the MIT license but can be changed to any other license that is available on the [choosealicense.com](https://choosealicense.com) website
- a gitignore file, default containing the standard python gitignore fields
- a README file, default containing a simple template that you can modify
- a pyproject.toml file, default containing the standard fields for a python package. This file is only created if you choose to create a python package or a python app.
- a setup.cfg file, default containing the standard fields for a python package. This file is only created if you choose to create a python package or a python app.
- a setup.py file, default containing the standard fields for a python package. This file is only created if you choose to create a python package or a python app.
- a directory structure, default containing a simple python package with a simple module and a simple test module. This directory structure is only created if you choose to create a python package or a python app. The directory structure is composed of a package directory, a test directory, every `__init__.py` file needed, and a simple module and a simple test module.
- If needed, this package can also create a simple Dockerfile that you can use to containerize your python app.

> [!NOTE]
> The `pyproject.toml`,`setup.cfg`, and `setup.py` files are optional and cannot be created together. If you choose to use a `pyproject.toml` project file (which is the new standard for python projects), the other two files will not be created. If you choose to use a `setup.cfg` file, the `setup.py` file will be created and not the `pyproject.toml` file.

## INSTALLATION

You can either clone the repository and install the package from the source code, or you can install it from pypi.

```bash
pip install pyproject-init
```

> [!NOTE]
> Note that the new recommended way to use and install packages is to use virtual environments, so you might want to create one before installing the package.

## USAGE

The package provide a command line interface with 2 main commands: `lib` and `app`. The `lib` command is used to create a simple python package, and the `app` command is used to create a python package with a CLI. Each of the commands has same options and arguments. Please refer to the help message or the documentation for more information.

```bash
pyproject-init lib --help
```

```bash
pyproject-init app --help
```

## EXAMPLES

Here are some examples of how to use the package.

### Create a simple python package

```bash
pyproject-init lib my_package
```

This will create a directory structure and files for a simple python package. The directory structure will look like this:

```bash
my_package/
    my_package/
        __init__.py
    tests/
        __init__.py
        test_my_package.py
    LICENSE
    .gitignore
    README.md
    pyproject.toml
    setup.cfg
    setup.py
```

### Create a python package with git initialized

This command line will create a simple python package and initialize a git repository in the directory.

```bash
pyproject-init lib my_package --git
```

### Create a python package with a Dockerfile

This command line will create a simple python package and a Dockerfile in the directory.

```bash
pyproject-init lib my_package --docker
```

### Create a python package with a different license

This command line will create a simple python package with a different license. The license must be available on the [choosealicense.com](https://choosealicense.com) website.

```bash
pyproject-init lib my_package --license gpl-3.0
```

### Create a python package with pyproject.toml

This command line will create a simple python package with a `pyproject.toml` file instead of the `setup.cfg` and `setup.py` files.

```bash
pyproject-init lib my_package --pyproject
```

### Create a python package with

## CONTRIBUTING

If you want to contribute to this project, you can either open an issue or a pull request. Please refer to the CONTRIBUTING.md file for more information.

## LICENSE

This project is licensed under the MIT license. Please refer to the [LICENSE](./LICENSE) file for more information.

## AUTHOR

This project was created by Quentin Haenn. You can contact me at [quentin.haenn.pro@gmail.com](mailto:quentin.haenn.pro@gmail.com?subject=pyproject-init).