import tkinter as tk
from datetime import datetime

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text=now)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Clock")

# フルスクリーンにする
root.attributes("-fullscreen", True)

label = tk.Label(root, font=("Arial", 100), fg="white", bg="black")
label.pack(expand=True)

update_time()
root.mainloop()
