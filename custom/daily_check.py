"""
每日检查工具模块
"""

from maa.custom_action import CustomAction


class DailyCompleteCheck(CustomAction):
    """检查每日任务是否全部完成"""

    def run(self, context, argv):
        """
        OCR 读取每日实训进度条
        返回是否已完成全部每日任务
        """
        # TODO: 实现每日任务进度 OCR
        # result = context.run_recognition("OCR", roi=daily_progress_roi)
        # completed = "500/500" in result or "全部完成" in result

        print("[每日检测] 检查每日任务进度...")
        return True
