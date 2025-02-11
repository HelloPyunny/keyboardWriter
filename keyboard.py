import pyautogui
import time
import random
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw() 
text = simpledialog.askstring("텍스트 입력", "입력할 텍스트를 입력하세요:")

print("5초 후 입력이 시작됩니다. 원하는 문서를 클릭하세요.")
time.sleep(5)

#pyautogui.typewrite(text, interval=0.1)

for char in text:
    pyautogui.typewrite(char)
    time.sleep(random.uniform(0.05, 0.2))