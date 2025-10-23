import os
from moviepy.editor import VideoFileClip

# 获取当前脚本所在的目录
folder_path = os.getcwd()

# 支持的视频格式
video_exts = (".mp4", ".mov", ".mkv", ".avi", ".flv", ".wmv")

for filename in os.listdir(folder_path):
    if filename.lower().endswith(video_exts):
        filepath = os.path.join(folder_path, filename)
        try:
            clip = VideoFileClip(filepath)
            duration = clip.duration  # 秒
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            print(f"{filename} —— {minutes}分{seconds}秒")
            clip.close()
        except Exception as e:
            print(f"{filename} 读取失败: {e}")

