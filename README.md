# get-comics
CLI tool for downloading comics from https://getcomics.org/


## Development setup

1. Clone the repository to your local machine

2. Setup the virtual environment
```sh
cd get-comics/
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/pre-commit install
```

3. Setup an editable version of the package

```sh
.venv/bin/python -m pip install --editable .
```

## TODO

- [ ] Download support
  - [x] Get all download links available
  - [ ] Support downloads from [Mega](https://pypi.org/project/mega.py/)
