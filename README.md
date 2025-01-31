# create and activate venv

```
python3.10 -m venv {venv_name}
source {venv_name}/bin/activate
```

# install dependencies

```
pip install --upgrade pip
pip install -r requirements.txt

# for testing
pip install -r requirements_test.txt
```

# run uvicorn server

```
uvicorn app.main:app --reload
```

# running .py & pytest

a. run as module (-m)

```
python -m app.main # don't include .py extension

# for running pytest explicitly, need to go for the alternative approach below
```

[alternatively]

b. export the root directory to python path

```
# probably need to run at each new terminal session
export PYTHONPATH="/path/to/hotel_transylvania"  # for linux & macOS
set PYTHONPATH=/path/to/hotel_transylvania # for windows cmd
$env:PYTHONPATH = "/path/to/hotel_transylvania" # for windows powershell
```

now can run:

```
# run .py
python app/main.py

# run pytest
pytest
pytest tests/testfile.py
```

[alternatively: configure pytest]

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
