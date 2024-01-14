# Templates. TravelWeb©

## Use Python 3.11.5

1. Install pyenv

2. Switch to Python 3.11.5
```
pyenv install 3.11.5
```
```
pyenv local 3.11.5
```
## Run app
```
cp .env-example .env
```
```
pip install poetry
```
```
poetry install
```
```
poetry run alembic upgrade head
```
```
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```
## Or use Taskfile
enjoy.