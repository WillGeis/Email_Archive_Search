@echo off
REM Change to the script's directory
cd /d "%~dp0"

REM Creates temp python script to check dependencies
set TEMP_PY=%TEMP%\\\\check_deps_temp.py
echo import subprocess > "%TEMP_PY%"
echo import sys >> "%TEMP_PY%"
echo required = ["extract_msg","easyocr","pdf2image","Pillow"] >> "%TEMP_PY%"
echo for package in required: >> "%TEMP_PY%"
echo     try: >> "%TEMP_PY%"
echo         __import__(package) >> "%TEMP_PY%"
echo         print(f"{package} already installed.") >> "%TEMP_PY%"
echo     except ImportError: >> "%TEMP_PY%"
echo         print(f"{package} not found, installing...") >> "%TEMP_PY%"
echo         subprocess.check_call([sys.executable, "-m", "pip", "install", package]) >> "%TEMP_PY%"

REM run py script
python "%TEMP_PY%"

REM delete py script
del "%TEMP_PY%"

REM run main
python ./core/Windowbuilder.py
pause
