import os
from ultralytics import YOLO

# 解决 OpenMP 冲突
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

if __name__ == '__main__':
    # Load a COCO-pretrained YOLOv8s model
    # 加载预训练的YOLOv8s模型
    model = YOLO("yolov8s.pt")

    # Display model information (optional)
    model.info()

    # Train the model on the COCO8 example dataset for 100 epochs
    results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

    # Run inference with the YOLOv8s model on a test image
    # 使用内置的测试图像
    results = model("ultralytics/assets/bus.jpg")