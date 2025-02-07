import pyautogui
import time



def type_with_delay(text, delay=0.0002):
    for character in text:
        if character == "\n":
            
            time.sleep(.5)
       
        pyautogui.write(character)
        time.sleep(delay)  
       

print("Switch to your Google Doc window")
time.sleep(5)

with open("./test.txt", "r") as file:
    text = file.read()

type_with_delay(text)