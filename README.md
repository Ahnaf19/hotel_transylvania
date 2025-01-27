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

# running .py

a. use module -m

```
python -m app.main # don't include .py extension
```

[alternatively]

b. export the root directory to python path

```
export PYTHONPATH=/path/to/hotel_transylvania # probably need to run at each new terminal session
```

now can run:

```
python app/main.py
```
