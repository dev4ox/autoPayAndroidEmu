set VENV_PATH=venv

set PYTHON_EXE=%~dp0%VENV_PATH%\Scripts\python.exe

powershell -Command "Start-Process '%PYTHON_EXE%' -ArgumentList 'main.py' -Verb RunAs"