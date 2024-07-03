@echo off

REM Set the name of the virtual environment directory
set "ENV_DIR=venv"

REM Check if the virtual environment directory exists
if not exist %ENV_DIR% (
    echo Virtual environment not found. Creating one...
    python -m venv %ENV_DIR%
)

REM Activate the virtual environment
call %ENV_DIR%\Scripts\activate

REM Install the requirements
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate

echo Setup complete.