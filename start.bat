@echo off

REM Check if the virtual environment directory exists
if not exist venv (
    echo Virtual environment not found. Creating one...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install the requirements if they are not already installed
pip install -r requirements.txt

REM Run the Python script
python main.py

REM Deactivate the virtual environment
deactivate

REM Keep the command prompt open after execution
pause
