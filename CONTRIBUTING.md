# 贡献指南

感谢你对 HonkaiStarRailAssistant 的关注！

## 贡献方式

### 🐛 报告问题

请通过 [Issues](https://github.com/928896993lhl/HonkaiStarRailAssistant/issues) 反馈：
- 描述问题发生的场景和步骤
- 提供 `debug/maa.log` 日志文件
- 注明游戏版本和分辨率设置

### 🚀 提交代码

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/你的功能`
3. 提交代码：
   - 遵循现有 Pipeline JSON 命名和结构
   - 运行 `python scripts/check_resource.py` 检查资源完整性
   - 新功能需同时更新 `interface.json` 的任务注册
4. 发起 Pull Request 到 `main` 分支

### 🖼️ 添加模板图片

1. 在游戏 1920×1080 窗口模式下截图
2. 裁剪出目标按钮/文字区域
3. 放入对应的 `assets/resource/base/image/[功能]/` 目录
4. PNG 格式，文件名用英文（如 `LoginButton.png`）

### 📋 添加 Pipeline 任务

参考 [MaaFramework Pipeline 协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md) 编写 JSON：

```json
{
    "任务名": {
        "recognition": "TemplateMatch",
        "template": "path/to/image.png",
        "action": "Click",
        "next": "下一个任务"
    }
}
```

### 🧠 编写自定义扩展

复杂的决策逻辑（如模拟宇宙祝福选择）使用 Python 自定义扩展：

```python
# custom/your_strategy.py
from maa.custom_recognition import CustomRecognition
from maa.custom_action import CustomAction

class YourLogic(CustomRecognition, CustomAction):
    def analyze(self, context, argv):
        # OCR 识别阶段
        pass

    def run(self, context, argv):
        # 动作执行阶段
        pass
```

然后在 `custom/__init__.py` 中注册。

---

## 环境搭建

```bash
git clone --recursive https://github.com/928896993lhl/HonkaiStarRailAssistant.git
cd HonkaiStarRailAssistant

# 下载 MaaFramework Release 包，解压到 deps/
python install.py
```

---

## 开发资源

- [MaaFramework 文档](https://docs.maa.plus/)
- [Pipeline 协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md)
- [M9A 参考项目](https://github.com/MAA1999/M9A)
- [MaaStarRail 参考项目](https://github.com/VincenttHo/MaaStarRail)
