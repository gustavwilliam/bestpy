# Dev installation
```
git clone https://github.com/gustavwilliam/bestpy

# cd into the new project directory
cd bestpy

# Install requirements
poetry install

# Activate the virtual environment
poetry shell

# install pre-commit hooks
pre-commit install
```

# Testing
Directly in the terminal:
```
poetry run pytest
```

In the Poetry shell, through the terminal:

```
poetry shell
pytest
```
