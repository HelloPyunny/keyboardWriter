#!/bin/zsh
cd "$(dirname "$0")"

# Check for Python3 and show install guide if missing
if ! command -v python3 &> /dev/null; then
  echo "Python3 is not installed. Please install it from https://www.python.org/downloads/"
  exit 1
fi

# Install dependencies (pyautogui, etc.)
pip3 install --user -r requirements.txt

# Run the program
python3 keyboard.py
