"""
模拟宇宙策略逻辑 — 自定义识别与动作

处理模拟宇宙中的：
1. 祝福选择优先级
2. 事件选项决策
3. 商店购买策略
"""

import random
from maa.custom_recognition import CustomRecognition
from maa.custom_action import CustomAction


# ============== 祝福优先级配置 ==============
# 格式: (关键词, 权重), 权重越高越优先
BLESSING_PRIORITY = [
    ("智识", 100),       # 群体伤害
    ("欢愉", 90),         # 追加攻击
    ("巡猎", 80),         # 单体伤害/速度
    ("毁灭", 75),         # 生存+输出
    ("存护", 70),         # 护盾
    ("丰饶", 65),         # 治疗
    ("虚无", 60),         # DOT
    ("记忆", 55),         # 冻结
]


class SimulatedUniverseLogic(CustomRecognition, CustomAction):
    """模拟宇宙核心逻辑: 分析祝福选项并选择最佳"""

    def analyze(self, context, argv):
        """
        识别阶段: OCR 读取三个祝福选项的文本
        返回: {"blessings": ["祝福A", "祝福B", "祝福C"]}
        """
        # TODO: 实际实现需要调用 MaaFramework OCR API
        # image = context.tasker.controller.cached_image
        # result = context.run_recognition("OCR", roi=blessing_roi)
        return {"blessings": []}

    def run(self, context, argv):
        """
        动作阶段: 根据优先级选择最佳祝福并点击
        """
        blessings = argv.get("blessings", [])

        if not blessings:
            # 找不到祝福时随机点击
            context.click(640, 360)
            return True

        # 按优先级排序
        scored = []
        for blessing in blessings:
            score = 0
            for keyword, weight in BLESSING_PRIORITY:
                if keyword in blessing:
                    score = weight
                    break
            scored.append((blessing, score))

        scored.sort(key=lambda x: x[1], reverse=True)

        best_blessing = scored[0][0]
        print(f"[模拟宇宙] 选择祝福: {best_blessing} (权重: {scored[0][1]})")

        # TODO: 根据 best_blessing 在 OCR 结果中的位置计算点击坐标
        # context.click(x, y)
        return True


class UniverseEventHandler(CustomAction):
    """模拟宇宙事件处理"""

    def run(self, context, argv):
        """
        处理随机事件的选项
        优先选择: 获得祝福 > 获得奇物 > 回复生命 > 给钱
        """
        # TODO: 实现事件文本 OCR 和决策逻辑
        print("[模拟宇宙] 处理事件...")

        # 默认点击第一个选项
        context.click(640, 400)
        return True


class UniverseShopHandler(CustomAction):
    """模拟宇宙商店处理"""

    def run(self, context, argv):
        """
        商店: 优先购买祝福，其次奇物
        """
        # TODO: 实现商店 OCR 和购买逻辑
        print("[模拟宇宙] 处理商店...")

        # 默认点击第一个商品
        context.click(500, 350)
        return True
