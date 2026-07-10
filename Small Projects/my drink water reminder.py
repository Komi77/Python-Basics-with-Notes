from win10toast import ToastNotifier
import time
import win32com.client 




def speak_text(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)



def windows_notification(title, message, duration=10):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=duration, threaded=True)
    time.sleep(0.1)
    speak_text("Drink your bitch ass water NIGGGA!!")

    while toaster.notification_active():
        time.sleep(0.1)

while True:
    windows_notification("Alert", "Drink your bitch ass water NIGGGAAAAAAA!")
    time.sleep(7200) 
