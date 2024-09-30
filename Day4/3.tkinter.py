import tkinter as tk

window = tk.Tk()
window.title("This is my first Tk Project")
window.geometry(f"{400}x{400}")
window.resizable(True, False)

label = tk.Label(window, text="Good Morning!!")
label.pack()
label2 = tk.Label(window, text="Good Days!!")
label2.pack()

count = 0
def print_in_console():
    global count
    count += 1
    print(f"Button pushed {count}")

button = tk.Button(window, text="Push me", command=print_in_console)
button.pack()

window.mainloop()