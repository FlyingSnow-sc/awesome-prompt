@echo off
echo ========================================
echo   Awesome Prompts - Build EXE
echo ========================================
echo.

cd /d "%~dp0"
cd prompt_tool

echo [1/5] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.7+ from python.org/downloads
    echo Make sure to check "Add Python to PATH"
    pause
    exit /b 1
)
echo OK: Python found

echo.
echo [2/5] Installing dependencies...
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple

echo.
echo [3/5] Preparing prompt files...
if exist "prompts" rmdir /s /q "prompts"
mkdir "prompts"

echo Copying files...
for /d %%i in (..\*) do (
    if not "%%~nxi"=="prompt_tool" if not "%%~nxi"=="package" if not "%%~nxi"==".git" (
        xcopy "%%i" "prompts\%%~nxi\" /E /I /Y >nul
        echo   Copied: %%~nxi
    )
)

echo.
echo [4/5] Building EXE...
echo This may take a few minutes...
pyinstaller --clean --onefile --windowed --add-data "prompts;prompts" main.py

if errorlevel 1 (
    echo.
    echo Build failed! Trying backup method...
    echo.
    pyinstaller --clean simple.spec
)

if exist "dist\AwesomePrompts.exe" (
    echo.
    echo ========================================
    echo   SUCCESS!
    echo ========================================
    echo.
    echo EXE location:
    echo %cd%\dist\AwesomePrompts.exe
    echo.
    echo You can run it now!
    start "" "dist"
) else (
    echo.
    echo ERROR: EXE not found
    echo Please check error messages above
)

echo.
pause
