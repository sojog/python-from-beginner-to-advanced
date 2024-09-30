import tkinter as tk

window = tk.Tk()
window.title("This is my first Tk Project")
window.geometry(f"{400}x{400}")
window.resizable(True, False)

label = tk.Label(window, text="0")
label.pack()

count = 0
def print_in_console(increase:bool):
    global count
    if increase:
        count += 1 
    else:
        count -= 1 
    print(f"Button pushed {count}")
    label.config(text=f"{count}")

plus_button = tk.Button(window, text="+", command=lambda x=True:print_in_console(x))
plus_button.pack()

minus_button = tk.Button(window, text="-", command=lambda x=False:print_in_console(x))
minus_button.pack()

window.mainloop()