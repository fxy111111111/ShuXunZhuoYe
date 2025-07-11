from ultralytics import YOLO

a1=YOLO('yolov5s.pt')

a1.train(
    data=r'C:\Users\a1516\Downloads\yolov5-v5.0\cxk.yaml',
    epochs=300,
    imgsz=640,
    batch=16,
    device='cpu'
)

print('完成')
