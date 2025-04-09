@echo off
echo [1/3] 正在创建虚拟环境 .venv ...
python -m venv .venv

echo [2/3] 正在尝试激活虚拟环境...
call .venv\Scripts\activate.bat || (
    echo ❌ 无法激活虚拟环境，请手动运行以下命令：
    echo    PowerShell: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    echo 或运行 enable_powershell.bat 以解决
    pause
    exit /b
)

echo [3/3] 正在安装依赖 ...
pip install --upgrade pip
pip install -r requirements.txt

echo ✅ 初始化完成！
pause
