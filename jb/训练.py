from ultralytics import YOLO
# Load a COCO-pretrained YOLOv8n model
# 加载预训练的YOLOv8n模型
model = YOLO("yolov8s.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")