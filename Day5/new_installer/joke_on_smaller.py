from tkinter import Tk as tk_Tk, Label as tk_Label, Button as tk_Button
from json import loads as json_loads
from requests import get as requests_get

window = tk_Tk()
WIDTH = HEIGHT = 500
full_screen_width =  window.winfo_screenwidth()
full_screen_height =  window.winfo_screenheight()
x = full_screen_width // 2 - WIDTH // 2
y = full_screen_height  // 2 - HEIGHT // 2
window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

joke_label = tk_Label(window, text="")
joke_label.pack()

def request_joke(event):
    print(event)
    response = requests_get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
    json_dict = json_loads(response.content)
    new_joke = json_dict['joke']
    joke_label.config(text=new_joke)
    

joke_button = tk_Button(window, text="New Joke")
joke_button.pack()
joke_button.bind("<Button-1>", request_joke)

window.mainloop()