import win32com.client 
import time


def speak_text(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

names = ["Ali", "Hassan", "Hussein", "Zainab", "Fatima"]

for name in names:
    speak_text(f"Shoutout to {name}!")
    time.sleep(0.5)
