from tkinter import Tk, Frame, Label, Button
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
            label = tk.Label(root, image = photo)
            label.image = photo  # 保持对图片对象的引用，防止被垃圾回收
            label.pack()

# 主窗口初始化
root = Tk()
root.title("图片重命名")

# 按钮
button = Button(root, text="选择文件夹", command = open_dir)
button.grid(row=0, column=0, sticky="ew")  # 占据整个宽度

# 主体内容区域
row1 = Frame(root, bg="light blue")
row1.grid(row=1, column=0, sticky="nsew")  # 伸展以占据剩余空间

# 左侧面板
pic1 = Frame(row1, bg="light blue", width=100, height=100)
pic1.grid(row=0, column=0, sticky="ns")  # 从顶部到底部
# 设置尺寸

# 右侧面板
tag1 = Frame(row1, bg="light green", width=100, height=100)
tag1.grid(row=0, column=1, sticky="nsew")  # 伸展并占据宽度

# 设置权重使右侧面板水平拉伸
row1.columnconfigure(1, weight=1)

# 启动主循环
root.mainloop()