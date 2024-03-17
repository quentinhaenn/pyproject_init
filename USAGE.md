# Usage with examples

Here are some examples of how to use the package.

- [Usage with examples](#usage-with-examples)
  - [Help](#help)
  - [Creating a simple lib without any options](#creating-a-simple-lib-without-any-options)
  - [Creating a simple lib with setup.cfg and setup.py](#creating-a-simple-lib-with-setupcfg-and-setuppy)
  - [Creating a simple lib with a Dockerfile](#creating-a-simple-lib-with-a-dockerfile)
  - [Creating a simple lib with a different license](#creating-a-simple-lib-with-a-different-license)
  - [Creating a simple lib with git initialized](#creating-a-simple-lib-with-git-initialized)
  - [Creating a lib with virtual environment](#creating-a-lib-with-virtual-environment)
  - [Combining options](#combining-options)
  - [Creating apps](#creating-apps)

## Help

You can get help with the following command lines:

```bash
pyproject-init lib --help
```

This will display the help message for the `lib` command line:

```bash
Usage: pyproject-init lib [OPTIONS] PROJECT_NAME

  Create a library project

Options:
  --setup         If set, create a setup.py and a setup.cfg file, if not
                  creates pyproject.toml
  --git           Initialize a git repository
  --virtualenv    Create a virtualenv
  --docker        Create a docker file
  --license TEXT  Choose the license type
  -h, --help      Show this message and exit.
```

```bash
pyproject-init app --help
```

This will display the help message for the `app` command line:

```bash
Usage: pyproject-init app [OPTIONS] PROJECT_NAME

  Create an application project

Options:
  --setup         If set, create a setup.py and a setup.cfg file, if not
                  creates pyproject.toml
  --git           Initialize a git repository
  --virtualenv    Create a virtualenv
  --docker        Create a docker file
  --license TEXT  Choose the license type
  -h, --help      Show this message and exit.
```

## Creating a simple lib without any options
 
```bash
pyproject-init lib my_package
```

This yields the following directory structure:

```bash
my_package/
├── LICENSE
├── README.md
├── pyproject.toml
└── test
    ├── docs
    ├── src
    │   └── __init__.py
    └── tests
```

The `pyproject.toml` file will look like this:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

The first lines of the `README.md` file will look like this:

```markdown
# Your/absolute/path/to/my_package
This is the README file for the `<absolute/path/to/my_package>` project.
You can write here a description of your project.
Suggested sections:
- Presentation
- Installation
- Usage
- Contributing
- License
```

The LICENSE file will contain the MIT license.

## Creating a simple lib with setup.cfg and setup.py

```bash
pyproject-init lib my_package --setup
```

This yields the following directory structure:

```bash
my_package/
├── LICENSE
├── README.md
├── my_package
│   ├── docs
│   ├── src
│   │   └── __init__.py
│   └── tests
├── setup.cfg
└── setup.py
```

The `setup.cfg` file will look like this:

```toml
[metadata]
name = /Users/quentin/Documents/test-reamde
version = 0.1.0
author = Your Name
author_email = youremail@some.com
description = A short description of the project
long_description = file: README.md
long_description_content_type = text/markdown
url = url to the project
license = MIT

[flake8]
max-line-length = 120
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
```

The `setup.py` file will look like this:

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="/Users/quentin/Documents/test-reamde",
    version="0.0.1",
    author="Your Name",
    author_email="your email",
    description="A short description of the project",
    long_description=long_description,
    url="url to the project",
    license="MIT",
    install_requires=[put your requirements here],
    packages=["put your packages here"],
    keywords=["put your keywords here"],
    classifiers=[
        Put your classifiers here,
    ],
    include_package_data=True,
)
```

The README.md file and the LICENSE file will be the same as in the previous example.

## Creating a simple lib with a Dockerfile

```bash
pyproject-init lib --docker my_package
```

This yields the following directory structure:

```bash
my_package/
├── Dockerfile
├── LICENSE
├── README.md
├── my_package
│   ├── docs
│   ├── src
│   │   └── __init__.py
│   └── tests
└── pyproject.toml
```

The `Dockerfile` will look like this:

```dockerfile
# This is an example Dockerfile. Modify it to match your needs
# Use the official image as a parent image
FROM <image name>
ADD . /<container directory>
WORKDIR /<container directory>
# Install the dependencies
RUN pip install -r requirements.txt
# Run the application
CMD python app.py
```

All other files created remains unchanged with regards to previous examples.

## Creating a simple lib with a different license

```bash
pyproject-init lib --license gpl-3.0 my_package
```

The tree structure is the same as in the first example, but the LICENSE file will contain the GPL-3.0 license.

## Creating a simple lib with git initialized

```bash
pyproject-init lib --git my_package
```

This yields the following directory structure:

```bash
my_package/
├── .git
├── .gitignore
├── LICENSE
├── README.md
├── my_package
│   ├── docs
│   ├── src
│   │   └── __init__.py
│   └── tests
└── pyproject.toml
```

Note that the `.git` directory and the `.gitignore` file have been added to the directory structure.

The `.gitignore` file will look like this:

```gitignore
# Configuration files
.vscode/
.DS_Store

# pytest artifacts
*.pyc
__pycache__/
.pytest_cache/

# Coverage
htmlcov/
.coverage

# Distribution
build/
dist/
.eggs/
*.egg-info

# Documentation source build
doc/_build
# Virtual environment
<Path/to/my_package-env>
```

All other files created remains unchanged with regards to previous examples.

## Creating a lib with virtual environment

```bash
pyproject-init lib --virtualenv my_package
```

This yields the following directory structure:

```bash
my_package/
├── LICENSE
├── README.md
├── my_package
│   ├── docs
│   ├── src
│   │   └── __init__.py
│   └── tests
├── my_package-env/
└── pyproject.toml
```

The `my_package-env` directory is the virtual environment. You can activate it with the following command:

```bash
source my_package-env/bin/activate
```

All other files created remains unchanged with regards to previous examples.

## Combining options

You can combine as many options as you want. That said, with full options, the command line will look like this:

```bash
pyproject-init lib --setup --docker --license gpl-3.0 --git --virtualenv my_package
```

## Creating apps

You can also create apps project structure with the `pyproject-init` package. Here is an example:

```bash
pyproject-init app my_app
```

This yields the following directory structure:

```bash
my_app/
├── LICENSE
├── README.md
├── my_app
│   ├── app
│   │   └── __init__.py
│   ├── docs
│   └── tests
└── pyproject.toml
```

All files created remains unchanged with regards to previous examples.

> [!NOTE]
> Every previous example can be used with the `app` command line, and yields the same results, except for the diretories' names.
