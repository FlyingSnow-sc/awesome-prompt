@echo off
chcp 65001 >nul
echo ========================================
echo   Awesome Prompts 一键打包工具
echo ========================================
echo.

cd /d "%~dp0"
cd prompt_tool

echo [1/5] 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未找到Python！
    echo 请先从 python.org/downloads 下载安装Python 3.7+
    echo 安装时请勾选 "Add Python to PATH"
    pause
    exit /b 1
)
echo ✅ Python环境正常

echo.
echo [2/5] 安装依赖...
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
if errorlevel 1 (
    echo ⚠️  依赖安装可能有问题，但继续尝试...
)
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple

echo.
echo [3/5] 准备提示词文件...
if exist "prompts" rmdir /s /q "prompts"
mkdir "prompts"

echo 正在复制文件...
for /d %%i in (..\*) do (
    if not "%%~nxi"=="prompt_tool" if not "%%~nxi"=="package" if not "%%~nxi"==".git" (
        xcopy "%%i" "prompts\%%~nxi\" /E /I /Y >nul
        echo   ✓ 已复制: %%~nxi
    )
)

echo.
echo [4/5] 开始打包...
echo 这可能需要几分钟，请耐心等待...
pyinstaller --clean --onefile --windowed --add-data "prompts;prompts" main.py

if errorlevel 1 (
    echo.
    echo ❌ 打包失败！
    echo 尝试备用方案...
    echo.
    pyinstaller --clean AwesomePrompts.spec
)

if exist "dist\AwesomePrompts.exe" (
    echo.
    echo ========================================
    echo   ✅ 打包成功！
    echo ========================================
    echo.
    echo 📂 可执行文件位置:
    echo %cd%\dist\AwesomePrompts.exe
    echo.
    echo 您可以直接运行这个EXE文件了！
    start "" "dist"
) else (
    echo.
    echo ❌ 未找到生成的EXE文件
    echo 请查看上面的错误信息
)

echo.
pause
