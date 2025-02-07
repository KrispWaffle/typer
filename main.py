import pyautogui
import time
import re

def type_with_delay(text, delay=0.5):
    words = re.split(r"([\n])", text)
    
    for word in words:
        if word == "\n":
            time.sleep(2)  
        pyautogui.write(word, interval=0.001)  # interval between each char
        time.sleep(delay)

print("Switch to your Google Doc window...")
time.sleep(5)

with open("test.txt", "r") as file:
    text = file.read()

type_with_delay(text)
