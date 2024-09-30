
import tkinter as tk

window = tk.Tk()
full_screen_width =  window.winfo_screenwidth()
full_screen_height =  window.winfo_screenheight()
print("WIDTH:", full_screen_width)
print("HEIGHT:", full_screen_height)

WIDTH = HEIGHT = 500
x = full_screen_width // 2 - WIDTH // 2
y = full_screen_height  // 2 - HEIGHT // 2


window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

window.mainloop()