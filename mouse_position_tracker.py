import pyautogui
import tkinter as tk

def update_position():
    x, y = pyautogui.position()
    position_label.config(text=f'Mouse position: ({x}, {y})')
    window.geometry(f'+{x+20}+{y+20}')
    window.after(100, update_position)

def on_escape(event):
    window.destroy()

window = tk.Tk()
window.overrideredirect(True)
window.attributes('-topmost', True)

position_label = tk.Label(window, text='', font=('Helvetica', 12), bg='yellow')
position_label.pack()

window.bind('<Escape>', on_escape)

update_position()
window.mainloop()
