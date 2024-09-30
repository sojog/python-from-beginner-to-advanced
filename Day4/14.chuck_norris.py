import tkinter as tk
import json
import requests
from pprint import pprint

window = tk.Tk()

input = tk.Entry(window)
input.pack()

def request_joke(event):
    print(event)
    query = input.get()
    response = requests.get("https://api.chucknorris.io/jokes/search", params={"query":query})
    json_dict = json.loads(response.content)
    pprint(json_dict)
    new_jokes = []
    
    for i in json_dict['result']:
        new_joke = i['value']
        new_jokes.append(new_joke)

    jokes = "\n".join(new_jokes)

    with open("chuck_norris.txt", "a") as fwriter:
        fwriter.write(jokes + "\n")
    
    joke_label.config(text=jokes)


joke_button = tk.Button(window, text="Get new joke")
joke_button.pack()

joke_label = tk.Label(window, text="")
joke_label.pack()
joke_button.bind("<Button-1>", request_joke)

window.mainloop()