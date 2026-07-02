"""
资源完整性检查工具

检查所有 Pipeline JSON 引用的模板图片是否存在，
以及 Pipeline 文件格式是否正确。
"""

from pathlib import Path
import json
import sys

WORKING_DIR = Path(__file__).parent.parent
PIPELINE_DIR = WORKING_DIR / "assets" / "resource" / "base" / "pipeline"
IMAGE_DIR = WORKING_DIR / "assets" / "resource" / "base" / "image"


def check_pipeline_json():
    """检查所有 Pipeline JSON 文件格式"""
    errors = 0

    for pipeline_file in PIPELINE_DIR.glob("*.json"):
        try:
            with open(pipeline_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            # 检查每个任务的 recognition + template 组合
            for task_name, task_config in data.items():
                if task_name.startswith("_"):
                    continue

                # 检查 TemplateMatch 是否有 template 字段
                if task_config.get("recognition") == "TemplateMatch":
                    if "template" not in task_config:
                        print(f"⚠️  [{pipeline_file.name}] {task_name}: TemplateMatch 缺少 template")
                        errors += 1

                # 检查 next 是否指向有效的任务
                if "next" in task_config:
                    next_tasks = task_config["next"]
                    if isinstance(next_tasks, str):
                        next_tasks = [next_tasks]
                    for nt in next_tasks:
                        if nt and nt not in data:
                            print(f"⚠️  [{pipeline_file.name}] {task_name} → {nt}: 目标任务不存在")
                            errors += 1

        except json.JSONDecodeError as e:
            print(f"❌ [{pipeline_file.name}] JSON 格式错误: {e}")
            errors += 1

    return errors


def check_template_images():
    """检查 template 引用的图片是否存在"""
    missing = 0

    for pipeline_file in PIPELINE_DIR.glob("*.json"):
        with open(pipeline_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for task_name, task_config in data.items():
            if task_name.startswith("_"):
                continue

            if task_config.get("recognition") == "TemplateMatch":
                templates = task_config.get("template", [])
                if isinstance(templates, str):
                    templates = [templates]

                for tpl in templates:
                    img_path = IMAGE_DIR / tpl
                    if not img_path.exists():
                        print(f"❌ [{pipeline_file.name}] {task_name}: 模板图片缺失 → {tpl}")
                        missing += 1

    return missing


def check_interface_json():
    """检查 interface.json"""
    interface_path = WORKING_DIR / "assets" / "interface.json"

    if not interface_path.exists():
        print("❌ interface.json 不存在！")
        return 1

    try:
        with open(interface_path, "r", encoding="utf-8") as f:
            interface = json.load(f)

        # 检查必要字段
        required_fields = ["controller", "resource", "task"]
        for field in required_fields:
            if field not in interface:
                print(f"❌ interface.json 缺少必要字段: {field}")

        # 检查任务入口是否在 Pipeline 中存在
        for task in interface.get("task", []):
            entry_name = task.get("entry", "")
            pipeline_file = PIPELINE_DIR / f"{entry_name.lower()}.json"
            # 尝试匹配命名规则
            found = False
            for pf in PIPELINE_DIR.glob("*.json"):
                with open(pf, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if entry_name in data:
                    found = True
                    break

            if not found:
                print(f"⚠️  interface.json 任务 '{task['name']}' 的 entry '{entry_name}' 未找到对应的 Pipeline 定义")

    except json.JSONDecodeError as e:
        print(f"❌ interface.json JSON 格式错误: {e}")
        return 1

    return 0


if __name__ == "__main__":
    print("=" * 50)
    print("  资源完整性检查")
    print("=" * 50)
    print()

    errors = 0

    print("--- 检查 Pipeline JSON 格式 ---")
    errors += check_pipeline_json()
    print()

    print("--- 检查模板图片 ---")
    errors += check_template_images()
    print()

    print("--- 检查 interface.json ---")
    errors += check_interface_json()
    print()

    print("=" * 50)
    if errors == 0:
        print("  ✅ 所有检查通过！")
    else:
        print(f"  ❌ 发现 {errors} 个问题，请修复后再构建")
    print("=" * 50)

    sys.exit(0 if errors == 0 else 1)
