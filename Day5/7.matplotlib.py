import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.xlabel('This is X Axis')
plt.ylabel('This is Y Axis')
plt.plot(x, y, "y") # https://matplotlib.org/stable/gallery/color/named_colors.html
plt.show()