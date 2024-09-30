
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.geometry(f"{400}x{400}")

input = tk.Entry(window)
input.pack()

frame = tk.Frame(window)
frame.pack()

def change_value(increase):
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

plus_button = tk.Button(frame, text="+", command=lambda x=True: change_value(x))
plus_button.grid(row=0, column=0)

minus_button = tk.Button(frame, text="-", command=lambda x=False: change_value(x))
minus_button.grid(row=0, column=1)

window.mainloop()

