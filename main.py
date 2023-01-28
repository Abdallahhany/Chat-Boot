from tkinter import *
import speech_recognition as sr  # recognise speech
import webbrowser  # open browser
import playsound  # to play an audio file
import random
import os
from gtts import gTTS  # google text to speech
from time import ctime

# GUI
root = Tk()
root.title("Virtual Voice Assistant")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
BG_ENTRY = "#2C3E50"


def there_exists(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()  # initialise a recogniser


# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone as source
        r.energy_threshold = 500  # voice level number increse more sensitive
        r.adjust_for_ambient_noise(source, 1.2)  # noise cancel rate
        r.pause_threshold = 1
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)  # convert audio to text

        except sr.RequestError:
            speak('Sorry, the service is down')  # error: recognizer is not connected
        except sr.UnknownValueError:  # error: recognizer does not understand
            print('Recognizing..')
        print(f">> {voice_data.lower()}")  # print what user said
        return voice_data.lower()


# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-in')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data):
    # 1: greeting
    if there_exists(["hey", "hi", "hello", "wake up", "hai"], voice_data):
        greetings = ["hey", "hey, what's up? ", " how can I help you", "I'm listening", "hello"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT -->" + greet)
        speak(greet)
        return

        # 2: name
    if there_exists(["your name", "what i call you", "what is your name"], voice_data):
        res = "my name is Vavo stand for virtual assistance version One. what's your name?"
        txt.insert(END, "\n BOT -->" + res)
        name = record_audio(res)
        res2 = 'Nice to meet you ' + name
        speak(res2)
        txt.insert(END, "\n BOT -->" + res2)
        res3 = 'how can i help you ' + name
        speak(res3)
        txt.insert(END, "\n BOT -->" + res3)
        return

        # 3: Origin

    if there_exists(["who are you", "your inventor", "invented you", "created you", "who is your developer"],
                    voice_data):
        greetings = [
            "I am Virtual Voice Assistant",
            "I am developed by Abdallah as a voice assistance"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT -->" + greet)
        speak(greet)
        return

    if there_exists(["what is your age", "how old are you", "when is your birthday"], voice_data):
        greetings = ["I came into this world in december 2022"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT -->" + greet)
        speak(greet)
        return

        # 3: Take care's
    if there_exists(
            ["how's everything", "how ia everything", "how are you", "how are you doing", "what's up", "whatsup"],
            voice_data):
        greetings = ["I am well ...thanks for asking ", "i am well", "Doing Great"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT -->" + greet)
        speak(greet)
        return

        # 3: greeting
    if there_exists(["What are you doing", "what you doing", "doing"], voice_data):
        greetings = ["nothing", "nothing...,just working for you", "Nothing much"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT -->" + greet)
        speak(greet)
        return

        # 4.1: time
    if there_exists(
            ["what's  the time", "tell me the time", "what time is it", "what is the time", "time is going on"],
            voice_data):
        time = ctime().split(" ")[4].split(":")[0:2]
        print(time)
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        txt.insert(END, "\n BOT -->" + time)
        speak(time)
        return

        # 00:21 AM -> 12:21

        # 5: search wekiapedia
    if there_exists(["wikipedia"], voice_data):
        res = 'What do you want to search for?'
        txt.insert(END, "\n BOT -->" + res)
        search = record_audio(res)
        url = 'https://en.wikipedia.org/wiki/' + search
        webbrowser.get().open(url)
        res2 = 'Here is what I found for' + search
        txt.insert(END, "\n BOT -->" + res2)
        speak(res2)
        return

        # 5: search
    if there_exists(["do google", "search google", "on google", "search for", "in google"], voice_data):
        res = 'What do you want to search for?'
        txt.insert(END, "\n BOT -->" + res)
        search = record_audio(res)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        res2 = 'Here is what I found for' + search
        txt.insert(END, "\n BOT -->" + res2)
        speak(res2)
        return

        # 5.6: opening youtube
    if there_exists(["open the youtube", "open youtube"], voice_data):
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)
        res = 'Opening YouTube'
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        return

        # 5.7: opening google
    if there_exists(["open the  google", "open google"], voice_data):
        url = 'https://www.google.com/'
        webbrowser.get().open(url)
        res = 'Opening Google'
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        return

        # 5.7: opening gmail
    if there_exists(["open gmail", "open email", "open my email", "check email"], voice_data):
        url = 'https://mail.google.com/'
        webbrowser.get().open(url)
        res = 'Opening Gmail'
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        return

        # 5.5: find location
    if there_exists(["location"], voice_data):
        res = 'What is the location?'
        txt.insert(END, "\n BOT -->" + res)
        location = record_audio(res)
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        res2 = 'Opening map of ' + location
        txt.insert(END, "\n BOT -->" + res2)
        speak(res2)
        return

        # 6: search youtube
    if there_exists(["search youtube", "search the youtube", "search in youtube", "in youtube", "on youtube"],
                    voice_data):
        res = 'What do you want to search for?'
        txt.insert(END, "\n BOT -->" + res)
        search = record_audio(res)
        r.pause_threshold = 2
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        res2 = 'Here is what I found'
        txt.insert(END, "\n BOT -->" + res2)
        speak(res2)
        return

    if there_exists(["open zoom", "zoom meeting", "zoom"], voice_data):
        res = "Opening Zoom"
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        os.system("/usr/bin/zoom")
        return

    if there_exists(["open team viewer", "team viewer", "teamviewer", "viewer"], voice_data):
        res = "Opening team viewer"
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        os.system("/opt/teamviewer/tv_bin/script/teamviewer")
        return

    if there_exists(["open calendar", "calendar"], voice_data):
        res = "Opening Calender"
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        os.system("gnome-calendar")
        return

    if there_exists(["open calculator", "calculator"], voice_data):
        res = "Opening calculator"
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        os.system("gnome-calculator")
        return

    if there_exists(["open camera", "camera"], voice_data):
        res = "Opening Camera"
        txt.insert(END, "\n BOT -->" + res)
        speak(res)
        os.system("gnome-control-center camera")
        return

    # OS shutdown
    # if there_exists(["shutdown system", "system off", "shutdown the system", "system shutdown"]):
    #     speak('Okay system will off in 30 seconds')
    #     os.system("shutdown /s /t 30")

    if there_exists(["good", "thank you", "thanks", "well done"], voice_data):
        greetings = ["my pleasure", "Don't mention", "Thanks for your compliment", "No problem.",
                     "Thank you, it makes my day to hear that."]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT -->" + greet)
        speak(greet)
        return

    if there_exists(["exit", "quit", "sleep", "shut up", "close"], voice_data):
        greetings = ["Going offline ! you can call me Anytime", "Okay ,you can call me Anytime", "See you later",
                     "See you soon", "Have a good day."]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        txt.insert(END, "\n BOT --> " + greet)
        speak(greet)
        exit()

    else:
        res = " Sorry i didn't recognize what you said or typed "
        txt.insert(END, "\n BOT --> " + res)
        speak(res)


# Send function
def sendByText():
    send = "You -> " + e.get()
    txt.insert(END,  # represents the point immediately after the last character entered by the user.
               "\n" + send)
    respond(e.get())
    e.delete(0, END)


def sendByVoice():
    voice_data = record_audio()  # get the voice input
    send = "You -> " + voice_data
    txt.insert(END,  # represents the point immediately after the last character entered by the user.
               "\n" + send)
    respond(voice_data)  # respond


Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10  # same as padding
      , width=20).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)  # to center txt

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1,  # full size of scrollbar
                relx=0.980)  # position of scrollbar

e = Entry(root, bg=BG_ENTRY, fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=sendByText).grid(row=2, column=1)
Button(root, text="Record", font=FONT_BOLD, bg=BG_GRAY, command=sendByVoice).grid(row=3)

root.mainloop()
