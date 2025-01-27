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

# add repo root to python path

```
export PYTHONPATH=/path/to/hotel_transylvania
```
