import os
import datetime
import locale
import speech
import webbrowser
from subprocess import Popen
import time

class dateandtime():
    locale.setlocale(locale.LC_ALL, '')
    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%m")
    year = datetime.datetime.now().strftime("%Y")
    hour = datetime.datetime.now().strftime("%H")
    minute = datetime.datetime.now().strftime("%M")
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    dayname = datetime.datetime.now().strftime("%A")



def all_voice_commands():    
    while True:
        text=speech.get_audio()
        #swi
        if "merhaba" in text:
            speech.speak("Merhaba.")

        if "test" in text:
            speech.speak("Test başarılı")

        if "spotify aç" in text:
            speech.speak("Spotify açılıyor.")
            os.system("start spotify:")

        if "youtube aç" in text:
            speech.speak("Youtube açılıyor.")
            webbrowser.open("https://www.youtube.com",new=1)

        if "sitemi aç" in text:
            speech.speak("Siteniz açılıyor")
            webbrowser.open("https://erkanyildirim.online",new=2)

        if "sistemi kapat" in text:
            speech.speak("Sistem kapatılıyor")
            exit()

        if "mail aç" in text:
            speech.speak("Mail uygulamanız açılıyor.")
            os.system("start outlookmail:")

        if "saat kaç" in text:
            speech.speak("Saat şu an "+str(dateandtime.hour+" "+dateandtime.minute))
            print(str(dateandtime.hour+" "+dateandtime.minute))

        if "teşekkürler" in text:
            speech.speak("rica ederim")
            speech.wakeup()

        if "bugün günlerden ne" in text:
            speech.speak("Bugün günlerden "+str(dateandtime.dayname))

        if "hangi yıldayız" in text:
            speech.speak("Şu an "+str(dateandtime.year)+"yılındayız.")

        if "mail kapat" in text:
            speech.speak("Mail uygulaması kapatılıyor")
            #os.system("taskkill /IM HxOutlook.exe")
            mail_task_kill=os.popen("taskkill /IM HxOutlook.exe /F").read()
            print(mail_task_kill)
            if mail_task_kill in 'ERROR: The process "HxOutlook.exe" not found.':
                speech.speak("Uygulama zaten kapalı.")

        if "spotify kapat" in text:
            speech.speak("Spotify Kapatılıyor.")
            spotify_task_kill=os.popen("taskkill /IM Spotify.exe /F").read()
            if spotify_task_kill in "ERROR":
                speech.speak("Uygulama zaten kapalı")
        
        if "sitemi kapat" in text:
            speech.speak("Siteniz kapatılıyor")

        if "linkedin aç" in text:
        #     Popen("start chrome https://linkedin.com",shell=True)
        #     time.sleep(10)
        #     Popen('taskkill /F /IM chrome.exe',shell=True)
            os.system("start chrome")
            webbrowser.open_new("https://linkedin.com")
            
        if "youtube'da arama yap" in text:
            speech.speak("Ne aramamı istersin?")
            arama=speech.get_audio()
            webbrowser.open("https://www.youtube.com/results?search_query="+arama)
            speech.speak(arama+" aranıyor")
