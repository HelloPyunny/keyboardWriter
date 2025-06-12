# Keyboard Writer

A simple auto-typing program. It types the text you enter at your desired speed automatically.

_Easily bypasses detection tools that check for AI-generated content by typing manually like a human_ 😁

## Features

- GUI launcher (text input, typing speed control, start button)
- Simulates real keyboard input using pyautogui
- Can be run on macOS with a double-click

## Installation & How to Run

1. **Install Python 3**

   - macOS usually comes with Python 3 pre-installed. If not, download it from [python.org](https://www.python.org/downloads/).

2. **Grant Execute Permission**

   - In Terminal, run the following command to give execute permission to `run.command`:

     ```zsh
     chmod +x run.command
     ```

3. **Run the Program**
   - Double-click the `run.command` file. It will automatically install required packages and launch the GUI.
   - Or, you can run it directly from Terminal:
     ```zsh
     ./run.command
     ```

## How to Use

1. After launching, enter the text you want to auto-type in the input box.
2. Set the minimum/maximum delay (seconds) to control typing speed.
3. Click the "Start Typing" button. Typing will begin after 5 seconds.
4. Make sure to click the document window (Notepad, Word, etc.) where you want the text to be typed before it starts.

## Required Packages

- pyautogui
- tkinter (Python standard library)

All required packages will be installed automatically when you run `run.command`.
