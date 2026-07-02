<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue" alt="platform">
  <img src="https://img.shields.io/badge/license-AGPL--3.0-green" alt="license">
  <img src="https://img.shields.io/badge/MaaFramework-latest-purple" alt="MaaFramework">
  <img src="https://img.shields.io/github/v/release/Shasnow/StarRailAssistant?label=version" alt="version" style="display:none">
</p>

<h1 align="center">🚂 崩坏:星穹铁道助手</h1>
<h3 align="center"><i>Honkai: Star Rail Assistant</i></h3>

<p align="center">
  基于 <a href="https://github.com/MaaXYZ/MaaFramework">MaaFramework</a> 实现的 PC 端星穹铁道自动化助手<br>
  图像识别 + Win32 窗口控制，解放双手！
</p>

---

## ✨ 功能介绍

| 功能 | 状态 | 说明 |
|------|------|------|
| 🔑 登录游戏 | 🟢 可用 | 自动点击进入游戏，处理黑屏/加载/月卡弹窗 |
| ⚔️ 清体力 | 🟢 可用 | 刷遗器、经验材料、行迹材料，支持所有关卡选择 |
| 🎁 领取日常奖励 | 🟢 可用 | 每日实训、无名勋礼、邮件一键全领 |
| 📨 委托派遣 | 🟢 可用 | 自动收取已完成委托，派遣新委托 |
| ⭐ 历战余响 | 🟡 开发中 | 每周BOSS挑战 |
| 🌌 模拟宇宙 | 🟡 开发中 | 自动刷差分宇宙至积分上限 |
| 💰 货币战争 | 🟡 开发中 | 标准博弈 + 超频博弈 |
| 🔄 一键日常 | 🟡 开发中 | 登录→领奖→委托→清体力 全自动 |

---

## 🚀 快速开始

### 系统要求

- **Windows 10/11 64位**
- 游戏分辨率设置为 **1920×1080 窗口模式**
- [Visual C++ 可再发行组件包](https://aka.ms/vs/17/release/vc_redist.x64.exe)

### 下载安装

1. 前往 [Releases](https://github.com/928896993lhl/HonkaiStarRailAssistant/releases) 下载 `HonkaiStarRailAssistant-win-x86_64-vX.X.X.zip`
2. 解压到任意目录
3. 双击 `启动小助手.bat` 开始使用
4. 根据终端提示选择任务

### 从源码运行

```bash
# 1. 克隆项目（包含子模块）
git clone --recursive https://github.com/928896993lhl/HonkaiStarRailAssistant.git
cd HonkaiStarRailAssistant

# 2. 下载 MaaFramework Release 包
#    https://github.com/MaaXYZ/MaaFramework/releases
#    解压到 deps/ 目录

# 3. 安装
python install.py

# 4. 运行
cd install
MaaPiCli.exe
```

---

## 🛠️ 开发指南

### 项目结构

```
HonkaiStarRailAssistant/
├── assets/
│   ├── config/                 # MaaPiCli 配置文件
│   ├── interface.json         # MaaFramework 入口（任务定义+选项）
│   └── resource/base/
│       ├── image/             # 模板图片（按功能分目录）
│       │   ├── common/        # 通用图片（关闭、主页等）
│       │   ├── login/         # 登录相关
│       │   ├── combat/        # 战斗/副本
│       │   ├── daily/         # 日常奖励
│       │   ├── dispatch/      # 委托派遣
│       │   ├── universe/      # 模拟宇宙
│       │   └── weekly/        # 周常
│       ├── model/             # OCR 模型
│       └── pipeline/          # Pipeline JSON 定义
├── custom/                    # 自定义 Python 扩展
│   ├── __init__.py           # 注册入口
│   ├── universe_strategy.py  # 模拟宇宙策略
│   └── daily_check.py        # 每日检查
├── scripts/
│   └── check_resource.py     # 资源完整性检查
├── .github/workflows/ci.yml  # CI/CD 自动构建发布
├── install.py                # 构建安装脚本
├── configure.py              # OCR 模型配置
└── README.md
```

### 添加新功能

1. 在 `assets/resource/base/image/[功能名]/` 放入模板图片
2. 在 `assets/resource/base/pipeline/` 创建 Pipeline JSON
3. 在 `assets/interface.json` 注册任务入口
4. 运行 `python scripts/check_resource.py` 检查完整性

> 参考 [MaaFramework 开发文档](https://docs.maa.plus/) 和 [Pipeline 协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md)

---

## ⚠️ 免责声明

本软件是一个外部工具旨在自动化《崩坏：星穹铁道》的游戏玩法。它被设计成仅通过现有用户界面与游戏交互，并遵守相关法律法规。

本软件不会以任何方式修改任何游戏文件或游戏代码。

本软件开源、免费，仅供学习交流使用。使用本软件产生的所有问题与本项目与开发者团队无关。

请注意，根据米哈游的 [崩坏:星穹铁道的公平游戏宣言](https://sr.mihoyo.com/news/111246):

> "严禁使用外挂、加速器、脚本或其他破坏游戏公平性的第三方工具。"
> "一经发现，米哈游将视违规严重程度及违规次数，采取扣除违规收益、冻结游戏账号、永久封禁游戏账号等措施。"

---

## 📄 许可证

本项目基于 [GNU Affero General Public License v3.0](LICENSE) 开源，由 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 强力驱动。

---

## 🙏 致谢

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework) — 通用游戏自动化框架
- [MaaStarRail](https://github.com/VincenttHo/MaaStarRail) — 本项目早期的 Pipeline 参考
- [March7thAssistant](https://github.com/moesnow/March7thAssistant) — 功能设计参考
