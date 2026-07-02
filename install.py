"""
HonkaiStarRailAssistant 安装/构建脚本
基于 MaaFramework，将项目资源打包为可发布结构
"""

from pathlib import Path
import shutil
import sys
import json
from configure import configure_ocr_model

working_dir = Path(__file__).parent
install_path = working_dir / Path("install")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.1.0"


def check_deps():
    """检查 MaaFramework 依赖"""
    deps_bin = working_dir / "deps" / "bin"

    if not deps_bin.exists():
        print("=" * 50)
        print("未找到 MaaFramework 依赖！")
        print("=" * 50)
        print()
        print("请从以下地址下载 MaaFramework Release 包：")
        print("  https://github.com/MaaXYZ/MaaFramework/releases")
        print()
        print("下载后解压到 deps/ 目录，结构应为：")
        print("  deps/")
        print("    bin/              ← 二进制文件")
        print("    share/MaaAgentBinary/  ← Agent 二进制")
        print()
        print("推荐下载: MaaFramework-win-x86_64-vX.X.X.zip")
        sys.exit(1)

    print(f"找到 MaaFramework 依赖: {deps_bin}")


def install_deps():
    """安装 MaaFramework 依赖库"""

    deps_bin = working_dir / "deps" / "bin"
    deps_agent = working_dir / "deps" / "share" / "MaaAgentBinary"

    # 复制二进制文件（排除不必要的控制器）
    shutil.copytree(
        deps_bin,
        install_path,
        ignore=shutil.ignore_patterns(
            "*MaaDbgControlUnit*",
            "*MaaThriftControlUnit*",
            "*MaaRpc*",
            "*MaaHttp*",
        ),
        dirs_exist_ok=True,
    )

    # 复制 Agent 二进制
    if deps_agent.exists():
        shutil.copytree(
            deps_agent,
            install_path / "MaaAgentBinary",
            dirs_exist_ok=True,
        )
        print("Agent 二进制复制完成")


def install_resource():
    """安装资源文件：模型、模板图片、Pipeline"""

    # 配置 OCR 模型
    configure_ocr_model()

    # 复制 resource 目录
    resource_src = working_dir / "assets" / "resource"
    resource_dst = install_path / "resource"

    shutil.copytree(resource_src, resource_dst, dirs_exist_ok=True)

    # 复制并更新 interface.json
    interface_src = working_dir / "assets" / "interface.json"
    interface_dst = install_path / "interface.json"
    shutil.copy2(interface_src, interface_dst)

    # 写入版本号
    with open(interface_dst, "r", encoding="utf-8") as f:
        interface = json.load(f)

    interface["version"] = version

    with open(interface_dst, "w", encoding="utf-8") as f:
        json.dump(interface, f, ensure_ascii=False, indent=4)

    print(f"资源文件安装完成 (版本: {version})")


def install_config():
    """安装配置文件"""

    config_src = working_dir / "assets" / "config" / "maa_pi_config.json"
    config_dst = install_path / "config" / "maa_pi_config.json"

    config_dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(config_src, config_dst)

    print("配置文件安装完成")


def install_chores():
    """安装杂项文件"""

    for filename in ["README.md", "LICENSE", "CHANGELOG.md"]:
        src = working_dir / filename
        if src.exists():
            shutil.copy2(src, install_path / filename)

    print("杂项文件安装完成")


def create_launcher():
    """创建启动批处理文件"""

    launcher = install_path / "启动小助手.bat"
    with open(launcher, "w", encoding="gbk") as f:
        f.write("@echo off\n")
        f.write("chcp 65001 >nul\n")
        f.write("title 崩坏:星穹铁道助手\n")
        f.write("echo =====================================\n")
        f.write("echo   崩坏:星穹铁道自动化助手\n")
        f.write("echo   Honkai: Star Rail Assistant\n")
        f.write("echo =====================================\n")
        f.write("echo.\n")
        f.write("echo 请确保游戏已启动，并处于 1920x1080 窗口模式\n")
        f.write("echo.\n")
        f.write("MaaPiCli.exe --config config/maa_pi_config.json\n")
        f.write("pause\n")

    print(f"启动器创建完毕: {launcher}")


if __name__ == "__main__":
    print("=" * 50)
    print("  HonkaiStarRailAssistant 构建脚本")
    print("=" * 50)
    print()

    check_deps()

    if install_path.exists():
        print(f"清理旧的安装目录: {install_path}")
        shutil.rmtree(install_path)

    install_path.mkdir(parents=True, exist_ok=True)

    install_deps()
    install_resource()
    install_config()
    install_chores()
    create_launcher()

    print()
    print("=" * 50)
    print(f"  构建成功！文件位于: {install_path}")
    print("  运行 启动小助手.bat 开始使用")
    print("=" * 50)
