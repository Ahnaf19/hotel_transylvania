# Welcome to Hotel Transylvania!

## Introduction

This repository contains the codebase for a web application built using FastAPI and Uvicorn. The application consists of simple scalable APIs for guests and rooms, can be integrated to manage hotel reservations and related functionalities. This documentation guides through the processes of setting up the development environment, installing dependencies, running the server, executing tests and incorporating CI unit testing using github actions.

> [!NOTE]
> Developed on `python 3.10.16`. Also tested and worked on [`3.11.11`, `3.12.8`, `3.13.1`]

This project highlights:

1. API for guests and rooms which was kinda fast to builld using `fastAPI`
2. Clean & modular repo structure
   - separate application and tests directory
   - clean module/package initiation at each submodule
   - modular directory structure for required data, schemas, services and routers
3. Clean application
   - Added multiple modular routers to the main
   - can be switched to any other framework easily
4. Use of proper data validation with `pydantic` and `type hints`
5. OOP approach for CRUD operations
6. Use of custom Exception using `fastapi.HTTPException`
7. Logging with `loguru`: what a library!
8. `pytest` for unit testing
9. Of course, `github actions` to automate testing (CI)
10. `Makefile` for professional project automation
11. Branch protection rule: need to create PR to push new codes to main and the PR triggers pass checks from the pytests

To be added:

- `code coverage` illustration of pytest testing
- code analysis using `codeql` in github actions
- implement `black`: auto formatting and check action

> [!TIP]
> Check the [Resources](#resources) section for a quick start on `FastAPI`, `Pydantic`, `Uvicorn`, `Loguru`, `Pytest` and `Makefile`.

## Project Setup

### Makefile Instructions

The repository includes a `Makefile` to simplify common tasks.

> might need to install `Makefile` beforehand.

#### Usage

To use the `Makefile`, run:

```
make [target]
```

Try running `make help` to see all available `targets`.

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

### run uvicorn server

```
uvicorn app.main:app --reload
```

### running .py & pytest

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
pytest tests/test_file_name.py
```

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

## Collaborate & Contribute

Bug reports, issues, forks and pull requests are always welcome!

## License

This project is available as open source under the MIT License. See the [LICENSE](./LICENSE) file for details.
