import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import io
from PIL import Image, ImageTk


window = tk.Tk()

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.xlabel('This is X Axis')
plt.ylabel('This is Y Axis')
plt.plot(x, y, "y") 

fig, ax = plt.subplots()
fig.savefig("testimage.png")


buffer = io.BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

new_image = Image.open(buffer)
photo = ImageTk.PhotoImage(new_image)


label = tk.Label(window, image=photo)
label.pack()

window.mainloop()