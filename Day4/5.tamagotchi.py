import tkinter as tk
import random
import time
from tkinter import messagebox

window = tk.Tk()

SQUARE = 500
x = (window.winfo_screenwidth() - SQUARE) // 2
y = (window.winfo_screenheight() - SQUARE) // 2
window.geometry(f"{SQUARE}x{SQUARE}+{x}+{y}")

status_label = tk.Label(window, text="I am NOT hungry!!!")
status_label.pack()

stop_time = None

def feed_tamagotchi():
    global stop_time, start_time
    stop_time = time.time()
    if start_time:
        delta = stop_time - start_time
        messagebox.showinfo(message=f"You won! You fed tamagotchi in {delta} secs")
    else:
        messagebox.showinfo(message=f"You lost! You pressed too soon")
        

feed_button = tk.Button(window, text="DO NOT feed me!!!", command=feed_tamagotchi)
feed_button.pack()

wait_seconds = random.randint(1, 5) * 1000
print(f"Waiting time: {wait_seconds}")

start_time = None

def start_game():
    global start_time
    print("The game has started..")
    status_label.config(text="I am hungry")
    feed_button.config(text="FEED me!!!")
    start_time = time.time()


status_label.after(wait_seconds, start_game)

window.mainloop()
