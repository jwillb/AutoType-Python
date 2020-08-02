import speech_recognition as sr
import pyaudio
import pyautogui as pygui
import keyboard as kb

# Create empty list for storing options
#options = []

# Retrieve options.txt (Not being used currently)
#with open ("options.txt", "rt") as settings:
#    for line in settings:
#        options.append(line)

# Specify Setting(s)

# mic_number = options[1]

# Initialize microphone and recognizer class
r = sr.Recognizer()
mic = sr.Microphone() # TODO Fix default micrphone function

while True:
    if kb.is_pressed("alt") and not kb.is_pressed("backspace") and kb.is_pressed("shift"):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Speak Now!")
            audio = r.listen(source) # TODO Change speech api to pocketsphinx or other open-source suite
            try:
                global transcription
                transcription = r.recognize_google(audio)
                print(transcription)
                pygui.write(transcription)
            except sr.UnknownValueError:
                print("Sorry, I don't understand.")