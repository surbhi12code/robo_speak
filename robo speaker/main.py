import os
import win32com.client as wincom

if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    print(" welcome to robo speaker made by surbhi")
    while True:

        x=input("enter your command")
        if x=="stop":
            break
        text=f" {x}"
        speak.Speak(text)



