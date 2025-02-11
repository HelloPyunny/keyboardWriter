import pyautogui
import time
import random
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw() 
text = simpledialog.askstring("Input Text", "Type in your text:")

print("click your docs, typing will start in 5 seconds.")
time.sleep(5)

#pyautogui.typewrite(text, interval=0.1)

for char in text:
    pyautogui.typewrite(char)
    time.sleep(random.uniform(0.05, 0.2))