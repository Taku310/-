import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# メインウィンドウの設定
root = tk.Tk()
root.title('Digital Clock')

# ラベルウィジェットの作成
clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
clock_label.pack(anchor='center')

# 時刻の更新
update_time()

# メインループの開始
root.mainloop()
