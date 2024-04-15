import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
import random
import os
import wikipedia
import sys

voiceEngine = pyttsx3.init()

# Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


# print(voices)

def speak(audio):  # here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir I am your Computer.")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir I am your Computer.")
    else:
        speak("Good evening sir I am your Computer.")

    # now convert audio to text


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising....")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:  # For Error handling
        speak("Network Connection Error...")
        print("Network connection error")
        return "none"
    return text


# for main function


if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "define" in query:
            speak("searching details....please wait")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")


        elif 'hotstar' in query:
            webbrowser.open("https://www.hotstar.com/in")
            speak("Ok sir opening hotstar")

        elif 'prime video' in query:
            webbrowser.open("https://www.primevideo.com/")
            speak("Ok sir opening prime video")

        elif 'netflix' in query:
            webbrowser.open("https://www.netflix.com/in/")
            speak("Ok sir opening netflix")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        elif 'good bye' in query:
            speak("good bye")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                      'i am okay ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okay' in ans_take_from_user_how_are_you:
                speak('okay..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Parth Khatkar Created me ! I give Lot of Thanks to Him "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am an AI based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello sir ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        elif query == 'none':
            continue

        elif 'play video' in query or 'open video' in query:
            temp = query.replace(' ', '+')
            g_url = "https://www.youtube.com/results?search_query="
            res_g = 'ok sir!'
            print(res_g)
            print(temp)
            print(g_url + temp)
            speak(res_g)
            webbrowser.open(g_url + temp)
            continue

        elif 'subscriptions' in query:
            g_url = "https://www.youtube.com/feed/subscriptions"
            res_g = 'ok sir!'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url)
            continue


        elif 'exit' in query or 'stop' in query or 'by' in query:
            ex_exit = 'Ok sir,Hoping to meet soon!'
            speak(ex_exit)
            exit()

        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = " Sorry I don't know the answer of the question but i will search from internet to give your answer ! answering..."
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url + temp)
