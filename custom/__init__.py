"""
模拟宇宙自定义策略模块

在 Pipeline JSON 中使用 Custom 识别/动作类型时，
MaaFramework 会调用此文件中的对应类。

注册方式: 在 MaaPiCli 或代码中调用 register_custom()
"""

from maa.custom_recognition import CustomRecognition
from maa.custom_action import CustomAction


def register_custom(maafw):
    """注册所有自定义识别器和动作到 MaaFramework"""

    from .universe_strategy import SimulatedUniverseLogic
    from .universe_strategy import UniverseEventHandler
    from .universe_strategy import UniverseShopHandler

    maafw.register_custom_recognition("SimulatedUniverseLogic", SimulatedUniverseLogic())
    maafw.register_custom_action("SimulatedUniverseLogic", SimulatedUniverseLogic())

    maafw.register_custom_action("UniverseEventHandler", UniverseEventHandler())
    maafw.register_custom_action("UniverseShopHandler", UniverseShopHandler())

    print("自定义模块注册完成")
