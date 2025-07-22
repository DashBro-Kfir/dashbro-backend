# dashbro-backend
This repository contains the main code for the Dashbro managment server responsible for:
[1] Managing the dashboard repository.
[2] Authentication.
[3]

## Development
To start developing make sure to install the required dependencies:
```bash
pip install .[test]
```

### Lint
This project uses ruff as it's linter. Make sure to follow the guidelines set in the ruff.toml.

To run ruff:
```bash
python -m ruff format .

python -m ruff check --fix .
```
