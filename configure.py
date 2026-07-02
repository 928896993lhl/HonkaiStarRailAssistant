"""
MaaFramework OCR 模型配置脚本
自动检测并下载适配的 OCR 模型
"""

from pathlib import Path
import json
import os

MODEL_DIR = Path(__file__).parent / "assets" / "resource" / "base" / "model"


def configure_ocr_model():
    """配置 OCR 模型，优先使用 ONNX Runtime GPU 加速"""

    if not MODEL_DIR.exists():
        MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # 检测可用推理引擎
    engines = _detect_available_engines()

    # 生成 OCR 配置
    ocr_config = {
        "recognition": "OCR",
        "model": "ppocr_v4",
        "backend": engines.get("preferred", "ONNXRuntime"),
        "device": engines.get("device", "CPU")
    }

    config_path = MODEL_DIR / "ocr_config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(ocr_config, f, ensure_ascii=False, indent=4)

    print(f"OCR 模型配置完成: {ocr_config['backend']} ({ocr_config['device']})")
    print(f"配置保存至: {config_path}")


def _detect_available_engines():
    """检测可用的 OCR 推理引擎"""

    engines = {
        "preferred": "ONNXRuntime",
        "device": "CPU"
    }

    try:
        import onnxruntime as ort
        providers = ort.get_available_providers()
        if "DmlExecutionProvider" in providers:
            engines["device"] = "DirectML"
            engines["preferred"] = "ONNXRuntime"
            print("检测到 DirectML 支持，将使用 GPU 加速")
        elif "CUDAExecutionProvider" in providers:
            engines["device"] = "CUDA"
            engines["preferred"] = "ONNXRuntime"
            print("检测到 CUDA 支持，将使用 GPU 加速")
    except ImportError:
        print("ONNX Runtime 未安装，将使用 CPU 推理")

    return engines


if __name__ == "__main__":
    configure_ocr_model()
