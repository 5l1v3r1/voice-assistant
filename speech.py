import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import allvoices

def speak(metin):
    tts=gTTS(text=metin,lang="tr")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")

def get_audio():
    chunk_size = 2048
    sample_rate = 48000
    r=sr.Recognizer()
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source: 
        r.adjust_for_ambient_noise(source) 
        r.energy_threshold
        print("Dinliyorum.")
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio,language="tr-tr")
            said=said.lower()
            print(said)
        except Exception as e:
            print("Exception: "+str(e))

        except Exception as recognizer_instance:
            print("")
    return said

def wakeup():
    while True:
        wake=get_audio()
        if "asistan uyan" in wake:
            speak("Merhaba, Dinliyorum!")
            allvoices.all_voice_commands()
