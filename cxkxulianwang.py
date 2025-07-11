#best.py效果最好的（用于应用）
##last.py训练到最后的（用于继续训练）
from ultralytics import YOLO

a1=YOLO(r'C:\Users\a1516\Downloads\yolov5-v5.0\runs\detect\train\weights\best.pt')
a1(r'C:\Users\a1516\Desktop\86775345-1-208.mp4',
   show=True,
   save=True,
   conf=0.5,
   imgsz=640
   )