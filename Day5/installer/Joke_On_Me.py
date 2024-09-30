import tkinter as tk
import json
import requests

window = tk.Tk()
WIDTH = HEIGHT = 500
full_screen_width =  window.winfo_screenwidth()
full_screen_height =  window.winfo_screenheight()
x = full_screen_width // 2 - WIDTH // 2
y = full_screen_height  // 2 - HEIGHT // 2
window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

joke_label = tk.Label(window, text="")
joke_label.pack()

def request_joke(event):
    print(event)
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
    json_dict = json.loads(response.content)
    new_joke = json_dict['joke']
    joke_label.config(text=new_joke)
    

joke_button = tk.Button(window, text="New Joke")
joke_button.pack()
joke_button.bind("<Button-1>", request_joke)

window.mainloop()