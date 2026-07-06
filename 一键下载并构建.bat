@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo =====================================
echo   MaaFramework 下载助手
echo =====================================
echo.

cd /d "%~dp0"

if exist "deps\bin\MaaPiCli.exe" (
    echo [OK] MaaFramework 已存在，跳过下载
    goto :build
)

echo [1/3] 正在获取最新版本号...
for /f "tokens=*" %%i in ('curl -sL https://api.github.com/repos/MaaXYZ/MaaFramework/releases/latest ^| python -c "import sys,json; print(json.load(sys.stdin)['tag_name'])"') do set "VERSION=%%i"

if "!VERSION!"=="" (
    echo [ERROR] 获取版本号失败，请检查网络或代理
    echo         手动下载: https://github.com/MaaXYZ/MaaFramework/releases
    pause
    exit /b 1
)

echo        最新版本: !VERSION!
echo.

set "URL=https://github.com/MaaXYZ/MaaFramework/releases/download/!VERSION!/MaaFramework-win-x86_64-!VERSION!.zip"
echo [2/3] 正在下载 MaaFramework !VERSION! ...
echo        URL: !URL!
echo.

mkdir deps 2>nul
curl -L --proxy http://127.0.0.1:7897 -o "deps\maafw.zip" "!URL!"

if not exist "deps\maafw.zip" (
    echo [ERROR] 下载失败，请检查代理设置
    pause
    exit /b 1
)

echo [3/3] 正在解压...
powershell -Command "Expand-Archive -Path 'deps\maafw.zip' -DestinationPath 'deps' -Force"
del "deps\maafw.zip" 2>nul

if exist "deps\bin\MaaPiCli.exe" (
    echo.
    echo [OK] MaaFramework 下载完成！
) else (
    echo.
    echo [WARN] 解压后未找到 MaaPiCli.exe，请检查 deps 目录结构
)

:build
echo.
echo =====================================
echo   正在构建项目...
echo =====================================
echo.
python install.py

if exist "install\MaaPiCli.exe" (
    echo.
    echo =====================================
    echo   构建完成！
    echo =====================================
    echo.
    echo 启动方式:
    echo   1. 打开星穹铁道 PC 端，设置 1920x1080 窗口模式
    echo   2. 双击 install\启动小助手.bat
    echo      或运行: cd install ^&^& MaaPiCli.exe
    echo.
) else (
    echo [ERROR] 构建失败，请检查上方错误信息
)

pause
