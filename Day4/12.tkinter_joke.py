import tkinter as tk
import json
import requests

window = tk.Tk()

joke_label = tk.Label(window, text="")
joke_label.pack()

def request_joke(event):
    print(event)
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
    json_dict = json.loads(response.content)
    new_joke = json_dict['joke']

    with open("jokes.txt", "a") as fwriter:
        fwriter.write(new_joke + "\n")
    
    joke_label.config(text=new_joke)
    

joke_button = tk.Button(window, text="New Joke")
joke_button.pack()
joke_button.bind("<Button-1>", request_joke)

window.mainloop()