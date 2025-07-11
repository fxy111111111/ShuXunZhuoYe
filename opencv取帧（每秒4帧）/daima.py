import cv2
import os

def extract_frames(video_path, output_folder, frames_per_second=4):

    os.makedirs(output_folder, exist_ok=True)
    
   
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"错误：无法打开视频文件！请检查路径：{video_path}")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    frame_interval = int(round(fps / frames_per_second))
    
    print(f"视频信息：{fps:.2f} FPS，总时长：{duration:.2f}秒")
    

    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:

            output_path = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            success = cv2.imwrite(output_path, frame)
            if not success:
                print(f"警告：无法保存图像到 {output_path}")
            saved_count += 1
        
        frame_count += 1
        print(f"\r处理进度：{frame_count}/{total_frames}帧", end="")
    
    cap.release()
    print(f"\n完成！共保存 {saved_count} 张图像到：{output_folder}")

if __name__ == "__main__":
  
    video_path = r'C:\Users\a1516\Desktop\蔡徐坤剪辑后取帧视频.mp4'
    output_folder = r'C:\Users\a1516\Desktop\cxksjj'
    
    extract_frames(video_path, output_folder, frames_per_second=4)