
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.geometry(f"{400}x{400}")

input = tk.Entry(window)
input.pack()

button = tk.Button(window, text="Request")
button.pack() 

def change_value(increase=True):
    value = input.get()
    try:
        value = int(value)
    except:
        messagebox.showerror(message="Please insert a number")
        return
    input.delete(0, tk.END)
    if increase:
        input.insert(0, f"{value+1}")
    else:
        input.insert(0, f"{value-1}")

button.bind("<Button>", change_value)

input.bind("<KeyRelease>", change_value)

window.mainloop()