#!/bin/zsh
cd "$(dirname "$0")"

# 파이썬3 확인 및 설치 안내
if ! command -v python3 &> /dev/null; then
  echo "Python3가 설치되어 있지 않습니다. https://www.python.org/downloads/ 에서 설치하세요."
  exit 1
fi

# pyautogui 등 의존성 설치
pip3 install --user -r requirements.txt

# 프로그램 실행
python3 keyboard.py
