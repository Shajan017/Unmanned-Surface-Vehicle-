"""
Waste detection module for the USV.

This script runs a YOLO model on frames from a camera and prints the
objects detected in the water-surface scene. The trained model file is
kept outside Git when it is large; see models/README.md.
"""

from pathlib import Path

from ultralytics import YOLO


MODEL_PATH = Path("models/best.pt")
CAMERA_SOURCE = 0
CONFIDENCE = 0.45


def run_detection() -> None:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}. Place the trained YOLO model there."
        )

    model = YOLO(str(MODEL_PATH))
    results = model.predict(source=CAMERA_SOURCE, conf=CONFIDENCE, stream=True)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[class_id]
            print(f"Detected: {class_name} | confidence={confidence:.2f}")


if __name__ == "__main__":
    run_detection()
