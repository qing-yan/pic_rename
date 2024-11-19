from tkinter import Tk, Frame, Label, Button

# 主窗口初始化
root = Tk()
root.title("Nested Grid Layout")

# 标题栏
title_frame = Frame(root)
title_frame.grid(row=0, column=0, sticky="ew")  # 占据整个宽度

# 标题
title_label = Label(title_frame, text="My App Title", font=("Arial", 20))
title_label.pack(fill="both")  # 居中显示

# 主体内容区域
content_frame = Frame(root)
content_frame.grid(row=1, column=0, sticky="nsew")  # 伸展以占据剩余空间

# 左侧面板
left_panel = Frame(content_frame, bg="light blue")
left_panel.grid(row=0, column=0, sticky="ns")  # 从顶部到底部

# 右侧面板
right_panel = Frame(content_frame, bg="light green")
right_panel.grid(row=0, column=1, sticky="nsew")  # 伸展并占据宽度

# 设置权重使右侧面板水平拉伸
content_frame.columnconfigure(1, weight=1)

# 添加按钮到侧边栏
button_left = Button(left_panel, text="Button Left", width=10)
button_left.pack(pady=(20, 0))

button_right = Button(right_panel, text="Button Right", width=10)
button_right.pack(expand=True, pady=20)

# 启动主循环
root.mainloop()