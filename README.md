# Templates. TravelWeb©

## Use Python 3.11.5

1. Install pyenv
##### Windows
```
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
##### Linux
```
curl https://pyenv.run | bash
```
```
pyenv init - | source
```
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


## Use Taskfile

#### Windows
Use PowerShell.
1. Install "Chocolatey":
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2. Install Taskfile:
```
choco install go-task
```
3. Reopen your terminal.
4. Use commands:
`code-format` - fast code format
`run-dev` - fast run dev server
