# Welcome to Hotel Transylvania!

## Table of Contents

1. [Introduction](#introduction)
2. [Project Setup](#project-setup)

- [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
- [Install Dependencies](#install-dependencies)
- [Makefile Instructions](#makefile-instructions)
- [Run Uvicorn Server](#run-uvicorn-server)
- [Running .py & Pytest](#running-py--pytest)
- [Generate Pytest Code Coverage](#generate-pytest-code-coverage)

3. [Continuous Integration (CI)](#continuous-integration-ci)

- [Implement GitHub Action Workflow for testing](#ci-implement-github-action-workflow-for-testing)
- [Code Formatting & Linting with Pre-commit](#ci-code-formatting--linting-with-pre-commit-black-isort-mypy)
- [Code Scanning with CodeQL](#ci-code-scanning-with-codeql)

4. [Resources](#resources)
5. [Collaborate & Contribute](#collaborate--contribute)
6. [License](#license)

## Introduction

This repository contains the codebase for a web application built using FastAPI and Uvicorn. The application consists of simple scalable APIs for guests and rooms, can be integrated to manage hotel reservations and related functionalities. This documentation guides through the processes of setting up the development environment, installing dependencies, running the server, executing tests and incorporating CI unit testing using github actions.

> [!NOTE]
> Developed on `python 3.10.16`. Also tested and worked on [`3.11.11`, `3.12.8`, `3.13.1`]

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

This project highlights:

1. `FastAPI` + `Uvicorn`: Lightning-fast API development for guests and rooms ⚡
2. Modular Architecture: Structured for scalability 🔥
   - separate application and tests directory
   - clean module/package initiation at each submodule
   - modular directory structure for required data, schemas, services and routers
3. Clean Application
   - Added multiple modular routers to the main
   - can be switched to any other framework easily
4. `Pydantic` + `Type Hints`: Strong data validation 💪
5. OOP-based CRUD: Maintainable and reusable service layers 🛠
6. Custom Exception Handling with `fastapi.HTTPException` 🚨
7. Logging with `Loguru`: Simplified yet powerful logging 📝
8. Automated Testing: `pytest` for unit tests 🔄
9. Code Coverage: `pytest-cov` for generating coverage metrics 📊
10. `GitHub Actions`: CI pipeline to ensure code quality ✅
11. `Makefile` for Automation: Professional project workflow ⚙️
12. Branch Protection Rules: PRs must pass checks before merging 🔐
13. Code Analysis using `codeql`: GitHub Actions & Python code vulnerability check 🤖
14. Code Auto-formatting & Linting with Pre-commit (check-yaml, end-of-file-fixer, trailing-whitespace, black, isort, mypy) 🎨

🛠 Upcoming Enhancements:

- [x] Code Coverage: `pytest-cov` for generating coverage metrics 📊
- [x] Static Code Analysis using `codeql` 🤖
- [x] Code Auto-formatting & Linting with Pre-commit (check-yaml, end-of-file-fixer, trailing-whitespace, black, isort, mypy) 🎨
- [ ] add pytest coverage in unit test action
- [ ] add action for format checks

> [!TIP]
> Check the [Resources](#resources) section for a quick start on `FastAPI`, `Pydantic`, `Uvicorn`, `Loguru`, `Pytest`, `Pytest-cov`, `Makefile`, `CodeQL`, `pre-commit` and `GitHub Actions`.

## Project Setup

### Create and Activate Virtual Environment

**Python Version**: Developed on `python 3.10.16`. Also tested and worked on [`3.11.11`, `3.12.8`, `3.13.1`]

```
# For Linux and macOS
python3.10 -m venv {venv_name}
source {venv_name}/bin/activate

# For Windows CMD
python -m venv {venv_name}
{venv_name}\Scripts\activate.bat

# For Windows PowerShell
python -m venv {venv_name}
{venv_name}\Scripts\Activate.ps1
```

### Install Dependencies

```
pip install --upgrade pip
pip install -r requirements.txt

# for testing
pip install -r requirements_test.txt
```

### Makefile Instructions

The repository includes a `Makefile` to simplify common tasks.

> might need to install `Makefile` beforehand.

#### Usage

To use the `Makefile`, run:

```
make [target]
```

Try running `make help` to see all available `targets`.

### Run Uvicorn Server

```
uvicorn app.main:app --reload
```

### Running .py & Pytest

a. run as module (-m)

```
# don't include .py extension
python -m app.main

# for running pytest explicitly, need to go for the alternative approach below
```

[alternatively]

b. export the root directory to python path

```
# probably need to run at each new terminal session

# for linux & macOS
export PYTHONPATH="/path/to/hotel_transylvania"

# for windows cmd
set PYTHONPATH=/path/to/hotel_transylvania

# for windows powershell
$env:PYTHONPATH = "/path/to/hotel_transylvania"
```

now can run:

```
# run .py
python app/main.py

# run pytest
pytest
pytest tests/
pytest tests/testfile.py
```

[alternatively: **configure pytest**]

add any one of `pytest.ini` or `tox.ini` or `setup.cfg` at root and add following:

```
[pytest]
pythonpath = .
```

Now, exporting the root path is not necessary, pytest would work. Try:

```
# run pytest
pytest
pytest tests/
pytest tests/test_file_name.py
```

### Generate Pytest Code Coverage

Generate code coverage report:

```
pytest --cov=[repo dir]

# for example:
pytest --cov=hotel_transylvania
```

Generate code coverage report HTML:

```
coverage HTML
```

This would write HTML report to `htmlcov/index.html`

### Continuous Integration (CI)

- unit testing using GitHub Actions
- Code formatting & linting with Pre-commit (black, isort, mypy)
- Code scanning with CodeQL

#### CI: Implement GitHub Action Workflow for testing

To automate the pytest testing using GitHub Actions, follow these steps:

1. Create a `.github/workflows` directory in the root of your repository if it doesn't already exist.

2. Inside the `.github/workflows` directory, create/add `.yml`/`.yaml` file that contains the workflow jobs. For example see: [unit_tests.yml](.github/workflows/unit_tests.yml)

3. Add event triggers like on push/pull request and branch/file filters according to need.

This workflow will trigger on every push and pull request to the `main` branch. It will set up Python 3.10, install the dependencies, and run the tests with coverage.

> [!TIP]
> Check the [Resources](#resources) `CI/GitHub Actions` section for more.

#### CI: Code Formatting & Linting with Pre-commit (black, isort, mypy)

To auto format the codebase, follow these steps:

1. at repo `root/` create a `.pre-commit-config.yaml` file. For example see: [.pre-commit-config.yaml](.pre-commit-config.yaml)
2. Add necessary repos and hooks to the `.yaml` file. In this repo following hooks are initiated:

- `check-yaml`: Validates YAML files for syntax errors.
- `end-of-file-fixer`: Ensures files end with a newline.
- `trailing-whitespace`: Removes trailing whitespace from files.
- `black`: Automatically formats code to adhere to PEP 8 standards.
- `isort`: Sorts and organizes imports in the code.
- `mypy`: Performs static type checking to ensure type correctness.

Don't forget to add the latest version/revision available for all hooks.

3. run the following command to set up the hooks, configured hooks will be run at each commit.

```
pre-commit install
pre-commit autoupdate
```

> [!NOTE]
> after pre-commit hooks are installed, every time `git commit` is run, the specified hooks will automatically check and format the code before allowing the commit.

> [!WARNING]
> If any check fails, corresponding hook will block the commit, make the required changes to be committed next.

> [!TIP]
> Check the [Resources](#resources) `CI/pre-commit Hooks` section for more.

##### Invoke Manual Format

```
# Format all directories
[black | isort | mypy --format] .

# Format a specific file or directory
[black | isort | mypy --format] path/to/file_or_directory
```

##### Invoke Manual Check

Run all pre-commit hooks:

```
# Check all formatting for all directories
pre-commit run --all-files

# Run for a specific directory or file
pre-commit run --files path/to/file_or_directory

# run explicit hook
pre-commit run black --all-files  # Only run Black
```

Run specific hook:

```
# Check formatting, import sorting, code style, and type checking for all directories
[black --check | isort --check-only | flake8 | mypy] .

# Check formatting, import sorting, code style, and type checking for a specific file or directory
[black --check | isort --check-only | flake8 | mypy] path/to/file_or_directory
```

##### Add, modify and Update hooks

> [!NOTE]
> To add or modify hooks, write accordingly in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file.

Auto udate hooks:

```
pre-commit autoupdate

```

#### CI: Code Scanning with CodeQL

From the `security` tab of the repo, enable `code scanning alert` with `default` configuration.

> [!TIP]
> Check the [Resources](#resources) `CI/CodeQL` section for more.

this now enables:

- ✅ Automated Security Scanning – Detects vulnerabilities and coding issues.
- ✅ Alerts for Security Issues – Displays issue type, severity, file location, and suggested fixes.
- ✅ PR & Push Scanning – Blocks insecure code from merging until fixed.
- ✅ Custom Query Support – Use CodeQL to define custom security checks.
- ✅ Integration with GitHub Actions – Automate scanning on every commit and PR.
- ✅ Security Insights & Compliance – Helps with secure coding practices and audits.

## Resources

- FastAPI official <a href="https://fastapi.tiangolo.com/learn/">documentation</a>

- learn basic usage of `fastAPI` & `Github Actions` from the following repo:

  - <a href="https://github.com/Ahnaf19/learn_fastapi">learn_fastapi</a>

- Learn about `Makefile` quickly from these awesome resources:

  - Guidance for installing it on: [<a href="https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows">Windows</a>, <a href="https://askubuntu.com/questions/161104/how-do-i-install-make">linux-unix</a>]
  - <a href="https://makefiletutorial.com/">makefile-tutorial</a>
  - <a href="https://www.youtube.com/watch?v=Yt-UF7fNLJE">youtube-NeuralNine</a>

- Data validation with `pydantic` <a href="https://docs.pydantic.dev/latest/api/base_model/">documentation-base_model</a>

- Custom exception handling with `fastapi.HTTPException` <a href="https://fastapi.tiangolo.com/tutorial/handling-errors/">handling-errors</a>

- Logging with `loguru` <a href="https://loguru.readthedocs.io/en/stable/">documentation</a>

- Running ASGI server with `uvicorn` <a href="https://www.uvicorn.org/">documentation</a>

- Testing with `pytest`:

  - Official <a href="https://docs.pytest.org/en/7.1.x/">documentation</a>
  - basic usage of `pytest` from this repo: <a href="https://github.com/Ahnaf19/learn_pytest">learn_pytest</a>

- Pytest Code Coverage with `pytest-cov`:

  - Coverage report generation with Pytest-cov <a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">documenation</a>

- CI:

  - GitHub Actions

    - <a href="https://docs.github.com/en/actions/about-github-actions/understanding-github-actions#the-components-of-github-actions">Components</a> of an Action
    - Official GitHub Actions <a href="https://docs.github.com/en/actions">documentation</a>
    - Learn <a href="https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow#about-workflow-triggers">triggering a workflow</a>
    - <a href="https://learnxinyminutes.com/yaml/">Learn</a> `yml` or `yaml` file
    - Frequently used community actions:
      - Clone repo in the workflow: <a href="https://github.com/actions/checkout">actions/checkout</a>
      - Set up python in the workflow: <a href="https://github.com/actions/setup-python">actions/setup-python</a>

  - Pre-commit Hooks (black, isort, mypy)

    - Follow the official pre-commit <a href="https://pre-commit.com/">quickstart documentation</a>
    - Find suitable <a href="https://pre-commit.com/hooks.html">hooks</a>

  - CodeQL

    - GitHub security <a href="https://docs.github.com/en/code-security/getting-started/github-security-features">features</a>
    - CodeQL <a href="https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning">default setup</a>

## Collaborate & Contribute

Bug reports, issues, forks and pull requests are always welcome!

## License

This project is available as open source under the MIT License. See the [LICENSE](./LICENSE) file for details.
