import pyautogui
import time
import random

size = pyautogui.size()
print(size)


# while True:
#     new_x = random.randint(0, size[0]) 
#     new_y = random.randint(0, size[1])
#     pyautogui.moveTo(new_x, new_y) 


for i in range(4):
    pyautogui.moveTo(30 , 30)
    time.sleep(2)
    pyautogui.moveTo(size[0] - 30, 30)
    time.sleep(2)
    pyautogui.moveTo(size[0] - 30, size[1] - 30)
    time.sleep(2)
    pyautogui.moveTo(30, size[1])
    time.sleep(2)

