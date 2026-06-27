import os
from ultralytics import YOLOWorld

# Fix Arch Wayland display issue
os.environ["QT_QPA_PLATFORM"] = "xcb"

# Load a pre-trained YOLO-World model
model = YOLOWorld("yolov8s-worldv2.pt")

# Set the custom class list to ONLY look for monkeys
model.set_classes(["monkey"])

print("YOLO-World initialized. Tracking monkeys only...")

# Track via webcam
model.track(source="0", show=True)
