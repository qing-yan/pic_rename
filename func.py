import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk


def open_dir():
    # 指定图片目录
    pic_dir = filedialog.askdirectory()
    # 遍历目录中的所有文件
    for file in os.listdir(pic_dir):
        # 检查文件是否为图片
        if file.endswith(".jpg") or file.endswith(".png"):
            # 加载图片
            image_path = os.path.join(pic_dir, file)
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            # 创建一个标签，用于显示图片
            label = tk.Label(root, image=photo)
            label.image = photo  # 保持对图片对象的引用，防止被垃圾回收
            label.pack()