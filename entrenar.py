from ultralytics import YOLO

modelo = YOLO("yolov8n.pt")
modelo.train(data="C:/contador-monedas/data.yaml", epochs=100, imgsz=640)
