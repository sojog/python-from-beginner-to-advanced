
import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="Red")
button1.grid(row=0, column=0)

button2 = tk.Button(window, text="Blue")
button2.grid(row=0, column=1)

button3 = tk.Button(window, text="Green")
button3.grid(row=0, column=2)


all_buttons = []
for index, el in enumerate(["AC", "+/-", "%"]):
    button = tk.Button(window, text=el)
    button.grid(row=1, column=index)
    all_buttons.append(button)


for index, el in enumerate(range(9, 0, -1)):
    print(f"index={index} el={el}")
    button = tk.Button(window, text=el)
    button.grid(row=2+index//3, column=2-index%3)  

zero_button = tk.Button(window, text="0")
zero_button.grid(row=6, columnspan=2, column=0, sticky="we")
window.mainloop()
