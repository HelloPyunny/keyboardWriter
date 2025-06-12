import pyautogui
import time
import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def start_typing(text, min_delay, max_delay):
    messagebox.showinfo(
        "Ready",
        "Click your document window. Typing will start in 5 seconds.\n\nIf typing does not work, check System Settings > Privacy & Security > Accessibility and make sure Python, Terminal, or your IDE is allowed."
    )
    root.after(5000, lambda: type_text(text, min_delay, max_delay))

def type_text(text, min_delay, max_delay):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(min_delay, max_delay))
    messagebox.showinfo("Done", "Typing is finished!")

def on_start():
    text = text_entry.get()
    try:
        min_delay = float(min_delay_entry.get())
        max_delay = float(max_delay_entry.get())
        if min_delay > max_delay:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter valid delay values.")
        return
    if not text:
        messagebox.showerror("Error", "Please enter some text.")
        return
    start_typing(text, min_delay, max_delay)

root = tk.Tk()
root.title("Keyboard Writer Launcher")
root.geometry("900x600")  # window size

label = tk.Label(root, text="Enter the text to auto-type: \n\n(ONLY ENGLISH)")
label.pack(pady=10)

text_entry = tk.Entry(root, width=70, font=("Arial", 18))
text_entry.pack(pady=80, ipady=80)

frame = tk.Frame(root)
frame.pack(pady=5)

min_delay_label = tk.Label(frame, text="Min delay (sec):")
min_delay_label.grid(row=0, column=0, padx=5)
min_delay_entry = tk.Entry(frame, width=5)
min_delay_entry.insert(0, "0.05")
min_delay_entry.grid(row=0, column=1, padx=5)

max_delay_label = tk.Label(frame, text="Max delay (sec):")
max_delay_label.grid(row=0, column=2, padx=5)
max_delay_entry = tk.Entry(frame, width=5)
max_delay_entry.insert(0, "0.2")
max_delay_entry.grid(row=0, column=3, padx=5)

start_button = tk.Button(root, text="Start Typing", command=on_start)
start_button.pack(pady=15)

info_label = tk.Label(root, text="Click your document window before starting!", fg="gray")
info_label.pack()

root.mainloop()