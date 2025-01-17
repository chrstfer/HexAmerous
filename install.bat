@echo off

REM Upgrading pip
call python -m pip install pip --upgrade
echo Done

REM Create a new virtual environment in the .venv folder
echo Creating a new Python virtual environment in the .venv folder
call python -m venv .venv
echo Done
call "%CD%\.venv\Scripts\activate.bat"

REM Install the required packages from requirements.txt
echo Installing required packages from requirements.txt
call pip install -r requirements.txt
echo Done

REM Install playwright
echo Installing playwright
call playwright install
echo Done

REM Run your Python script (chappy.py)
echo Running your Python script (chappy.py)
call python chappy.py