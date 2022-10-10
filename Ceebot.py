import time;
import webbrowser;
from datetime import datetime;
import calendar;
import os;
import turtle
import pyttsx3
import wikipedia
import smtplib
import requests
import random

username = "CeeBee803!";
timerCount = 10;
jokes = ['What sound did the fish make when boiled in a pressure cooker? - Fisssshhhhhhhhhh!',
         'What did one toilet say to the other? - You look flushed',
         'Why can\'t Elsa from Frozen have a balloon? - She will "let it go! let it go!"',
         'Why did the kid bring a ladder to school? - He wanted to go to high school',
         'How do you get a squirrel to like you? - Act like a nut',
         'How does a scientist freshen her breath? - With experi-mints',
         'What is a computer\'s favourite snack - Computer chips',
         'What did one volcano say to the other? - I lava my life',
         'How do we know that the ocean is friendly? - It waves',
         'How do you talk to a giant? - Use big words',
         'Knock-Knock, Who\'s there? - Tank, Tank who? - You\'re welcome',
         'Why was the baby strawberry crying? - Her mom and dad were in a jam ',
         'What did the little corn say to the mama corn? - Where is pop corn?',
         'What did the limestone say to the geologist? - Don\'t take me for granite',
         'What kind of tree fits in your hand? - A palm tree',
         'What do you call a dinosaur that is sleeping? - A dino-snore',
         'What did the left eye say to the right eye? - Between us, something smells...',
         'What did one plate say to the other plate? - Dinner is on me.',
         'Why did the student eat his homework? - The teacher told him it was a piece of cake',
         'What do you say to a rabbit on its birthday? - Hoppy Birthday',
         'Why is the obtuse triangle always so frustrated? - Its never right',
         'Why is six afraid of seven? - Seven eight nine',
         'Why was the equal sign so humble? - He wasn\'t greater than or less than anyone else'];

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour);
    if hour >= 0 and hour < 12:
        print("Good morning");
        speak("good morning");
    elif hour>=12 and hour < 18:
        print("Good afternoon");
        speak("Good afternoon");
    else:
        print("Good evening!");
        speak("Good evening");
    print("Hello this is Ceebot version 1.0, use `/help` for help and guides");
    speak("How may I help you today");

def search():
    q = input("How may I help you?: ").lower();
    if q == "/help":
        print("Commands possible in Ceebot ver 1.0 -");
        print("Open calendar - `calendar`");
        print("Open URLs in general - `/link`");
        print("Direct wikipedia searching - `wikipedia` + searchitem");
        print("Direct youtube searching through Ceebot - `/ytsearch`");
        print("Can open things like - Discord, Youtube, Spotify, Instagram, Facebook, Roblox, etc with `open + appname`");
        print("Tell jokes - `Tell a joke`");
    if "hi" in q or "hey" in q or "hello" in q:
        print("Hello " + username);
    if "what" and "time" in q or "date" in q:
        print(str(datetime.now()));
    if "open" and "chrome" in q:
        print("Opening Chrome");
        webbrowser.open("https://www.google.com");
    if q == "/sd":
      exit();
    if "open" and "youtube" in q:
      print("Opening youtube");
      webbrowser.open("https://www.youtube.com");
    if "open" and "spotify" in q:
      print("Opening spotify");
      webbrowser.open("https://open.spotify.com");
    if "calendar" in q:
      print(calendar.calendar(2022,2,1,6));
      print("The above is the 2022 calendar.")
    if "open" and "discord" in q:
      print("Opening discord");
      webbrowser.open("https://www.discord.com/channels/@me");
    if "open" and "instagram" in q:
      print("Opening instagram");
      webbrowser.open("https://instagram.com");
    if "open" and "google" and "chat" in q:
      print("Opening Google chat");
      webbrowser.open("https://chat.google.com");
    if "open" and "roblox" in q:
      print("Opening roblox");
      webbrowser.open("https://roblox.com");
    if "open" and "facebook" in q:
      print("Opening facebook");
      webbrowser.open("https://facebook.com");
    if "open" and "krunker" in q:
        print("Opening krunker");
        webbrowser.open("https://krunker.io");
        speak("Opening krunker");
    if "open" and "playlist" in q:
        print("Opening your playlist on spotify");
        webbrowser.open("https://open.spotify.com/playlist/6M2EzIo8pvGkcgmi5cY1SR");
        speak("Opening your playlist on spotify");
    if q == "/link":
      link = input("Please enter the URL of the site you want to open: ");
      print("Opening " + link);
      webbrowser.open(link);
    if q == "/ytsearch":
      ytQ = input("What do you want to search on youtube?: ")
      print("Searching for " + ytQ);
      webbrowser.open("https://www.youtube.com/results?search_query=" + ytQ);
    if "wikipedia" in q:
        speak("Searching wikipedia")
        q = q.replace("wikipedia", "")
        results = wikipedia.summary(q, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    if "play music" in q:
        music_dir = "C:\\Users\\user\\Documents\\CeeBee\\Media\\Music and audio"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    if "open" and "playstore" in q:
        webbrowser.open("https://play.google.com");
    if "bored" in q:
        print("I can play music, open applications and websites, browse, crack a few jokes and more, why dont you try them, " + username + "?");
    if "joke" in q:
        chosenJoke = random.choice(jokes);
        print(chosenJoke);
        speak(chosenJoke);
    if "start" and "timer" in q:
        timerCount = 5;
        timer();
    if q == "/spotifysearch":
        item = input("What would you like to search on spotify?");
        print("Searching for " + item);
        webbrowser.open("https://open.spotify.com/search/" + item);
        speak("Searching for " + item);
    if "good" and "morning" in q:
        print("Good morning, " + username);
        speak("Good morning, " + username);
        print("The time is " + str(datetime.now().hour) + ":" + str(datetime.now().minute));
        speak("The time is " + str(datetime.now().hour) + ":" + str(datetime.now().minute));
    search();

def timer():
    for count in range(1, timerCount + 1):
        time.sleep(1);
        print(count)
        if count == timerCount:
            print("Your timer is complete");
            speak("Your timer is complete")


wishMe();
search();
