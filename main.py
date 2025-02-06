import sys 
from time import sleep
f = open("test.txt", "r")
text = f.read()

letters = list(text)
print(letters)
waitT = 0
for i in range(len(letters)):
   
    if(waitT ==14 and letters[i] == ' '):
        sleep(3)
        waitT=0
    else:
        print(letters[i], end="",flush=True)
        sleep(0.01)
        waitT+=2

