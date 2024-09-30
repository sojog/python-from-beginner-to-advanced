
import tkinter as tk

window = tk.Tk()
width = 400
height  = 600 
x = 100
y = 200 

window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()