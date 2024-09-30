import tkinter as tk
import random
import time

options = ["cat", "dog", "pig", "tiger", "pet", "turtle"] * 2
# random.shuffle(options)
print(options)

root = tk.Tk()

stop_button = tk.Button(root, text="Stop")
stop_button.grid(row=0, column=0)

def restart_game():
    global all_buttons, last_pushed_button_index, revealed_button_indexes
    for index, button in enumerate(all_buttons):
        button.config(text=f"{index+1}")
    revealed_button_indexes.clear()
    last_pushed_button_index = None


restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=0, column=1)

exit_button = tk.Button(root, text="Exit")
exit_button.grid(row=0, column=2)

all_buttons = []
last_pushed_button_index = None

revealed_button_indexes = []
WAIT_SECS = 2 * 1000

should_wait = False

def switch_wait():
    global should_wait
    should_wait = not should_wait

def show_button(index):
    global last_pushed_button_index, revealed_button_indexes, should_wait
    if should_wait:
        return
    print(f" Button no {index} pushed")
    pushed_button = all_buttons[index]
    pushed_button.config(text=options[index])
    if not last_pushed_button_index:
        last_pushed_button_index = index
    elif last_pushed_button_index == index:
        return 
    elif options[last_pushed_button_index] == options[index]:
        print("You got it")
        revealed_button_indexes.extend([index, last_pushed_button_index])
        last_pushed_button_index = None
    else:
        print("You did not get it")
        should_wait = True 
        
        for i in (index, last_pushed_button_index):
            button:tk.Button = all_buttons[i]
            button.after(WAIT_SECS, lambda x=i: all_buttons[x].config(text=f"{x+1}") )
        last_pushed_button_index = None
        button.after(WAIT_SECS, switch_wait)
        
        
for i in range(12):
    button = tk.Button(root, text=f"{i+1}", command=lambda x=i:show_button(x))
    button.grid(row=1+i//3, column=i%3, sticky="we")
    all_buttons.append(button) 



root.mainloop()