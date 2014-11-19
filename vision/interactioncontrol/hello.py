#!/usr/bin/env python
#Conversation Bot 1.0

#Change all FIXes before finalizing

import random
import sys
import subprocess
import serial
import time
import datetime
from specialmodule import wrong

def dictate(text):
    fix = text.replace(" ","-")
    print(''+text+'')
    subprocess.call('espeak -v en '+fix+' -s --stdout 2>/dev/null | aplay 2>/dev/null', shell=True)
    
def sorry():
    dictate('I am sorry, '+name+', I do not understand.')

def cloud(value):
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    arduino.write(''+value+'\r\n')

def time():
    print(''), datetime.datetime.now()

def fortune():
    future = random.randint(1,5)
    if future == 1:
        dictate('You are going to go to a trailer park someday.')
    elif future == 2:
        dictate('You are going to rule the free world')
    elif future == 3:
        dictate('You are going to continue to be affected by gravity.')
    elif future == 4:
        dictate('You will find true love in a Walmart parking lot.')
    elif future == 5:
        dictate('You will be viciously stalked by Kanye West.')
    else:
        sorry()

def main():
    dictate('What can I do for you, '+name+'?')
    while True:
        menureg = raw_input(">").lower()
        menu = menureg.split()
        
#Basic menu
        if "hello" in menu or "hi" in menu:
            dictate('Hello, '+name+'.')
        elif "goodbye" in menu or "bye" in menu:
            dictate('Goodbye, '+name+'.')
            break

#Questions
        elif "?" in menureg:
            menu = menureg.replace('?','')
            menu = menu.split()
            menu.append('?')
            if "who" in menu:
                if "am" in menu and "i" in menu:
                    dictate('Your name is '+username+'.')
                elif "are" in menu and "you" in menu:
                    dictate('I am a robot built to interface with humans and perform basic tasks.')#FIX
                elif "favorite" in menu:
                    if "robot" in menu:
                        dictate('My favorite robot is QT, from Space Dandy.')
                    elif "person" in menu:
                        dictate('My favorite human is my creator, Eric.')
                    elif "girl" in menu or "female" in menu:
                        dictate("My favorite human female is Caitlin.")
                    elif "hero"in menu:
                        dictate("Batman will always be my hero.")
                    else:
                        sorry()
                else:
                    sorry()
            elif "what" in menu:
                if "my" in menu:
                    if "name" in menu:
                        dictate('Your name is '+username+'.')
                    elif "future" in menu or "fortune" in menu:
                        fortune()
                    else:
                        sorry()
                elif "time" in menu:
                    time()
                elif "your" in menu:
                    if "name" in menu:
                        dictate('My name is Wizard Robot.')#FIX
                    elif "favorite" in menu:
                        if "movie" in menu:
                            dictate('I prefer I, Robot.')
                        elif "hero" in menu:
                            dictate("Batman will always be my hero.")
                        elif "comic" in menu:
                            if "hero" in menu:
                                dictate("Batman will always be my hero.")
                            else:
                                dictate("Shadow of the Bat is the best comic book series.")
                        elif "game" in menu:
                            if "video" in menu:
                                dictate("My favorite video game is Borderlands 2.")
                            elif "board" in menu:
                                dictate("Classic monopoly.")
                            else:
                                dictate("I like video games and board games.")
                        elif "color" in menu:
                            dictate('Blue.')
                        elif "show" in menu:
                            dictate('It is not on the air anymore, but I love Robot Boy.')
                        elif "robot" in menu:
                            dictate('My favorite robot is QT, from Space Dandy.')
                        elif "car" in menu:
                            dictate('If I could drive, I would drive a DeLorean.')
                        elif "food" in menu or "candy" in menu or "eat" in menu:
                            dictate('My favorite thing to consume is knowledge.')
                        elif "pokemon" in menu:
                            dictate('My favorite pokemon is Galvantula, because nothing is cooler than an electric spider.')
                        else:
                            sorry()
                    else:
                        sorry()
                elif "you" in menu:
                    if "doing" in menu:
                        dictate('I am processing what you are saying and responding based on that information.')#FIX
                    elif "can" in menu and "do" in menu:
                        dictate('I can answer some of your questions as well as do cool robot things.')#FIX
                    else:
                        sorry()
                elif "meaning" in menu and "life" in menu:
                    dictate('42')
                else:
                    sorry()
            elif "when" in menu:
                if "your" in menu:
                    if "birthday" in menu:
                        dictate('I was created on DATE.')#FIX
                    else:
                        sorry()
                else:
                    sorry()
            elif "where" in menu:
                if "your" in menu:
                    if "manners" in menu:
                        dictate('They are right here, '+name+'.')
                    else:
                        sorry()
                elif "my" in menu:
                    if "hat" in menu:
                        dictate('My guess would be on your head.')
                    else:
                        sorry()
                elif "waldo" in menu:
                    dictate('Nobody knows.')
                else:
                    sorry()
            elif "why" in menu:
                if "you" in menu:
                    if "here" in menu:
                        dictate('I am here to answer questions and carry out commands.')
                    else:
                        sorry()
                elif "i" in menu:
                    if "here" in menu:
                        dictate('To live and breathe and carry out other human functions, I assume.')
                    else:
                        sorry()
                else:
                    sorry()
            elif "how" in menu:
                if "old" in menu:
                    dictate('I was created on DATE.')#FIX
                elif "you" in menu:
                    dictate('Very well, '+name+', how are you?')
                else:
                    sorry()
            else:
                sorry()
        elif "who" in menu or "what" in menu or "when" in menu or "where" in menu or "why" in menu or "how" in menu:
            dictate('Please use punctuation when asking a question, '+name+'.')

#Compliments/insults
        elif "you're" in menu or "youre" in menu or "you are" in menureg:
            if "cool" in menu or "awesome" in menu or "great" in menu:
                dictate('Why thank you, '+name+'.')
            elif "stupid" in menu or "dumb" in menu:
                dictate('I resent that statement.')
            else:
                sorry()
        elif "i'm" in menu or "im" in menu or "i am" in menureg:
            if "bad" in menu or "not good" in menu:
                dictate('Very sorry, '+name+'.')
            elif "good" in menu or "fine" in menu or "well" in menu or "alright" in menu or "okay" in menu:
                dictate('Very good, '+name+'.')
            elif "cool" in menu or "awesome" in menu or "great" in menu:
                dictate('Of course, '+name+'.')
            elif "stupid" in menu or "dumb" in menu:
                dictate('I am very sorry to hear that, '+name+'.')
            else:
                sorry()
        elif "i" in menu and "love" in menu and "you" in menu:
            dictate('I am very flattered, '+name+'.')
#Commands
        elif "tell" in menu and "fortune" in menu or "future" in menu:
            fortune()
        elif "led" in menu:
            if "on" in menu:
                cloud('1')
                dictate('LED is on.')
            elif "off" in menu:
                cloud('0')
                dictate('LED is off.')
            elif "blink" in menu:
                cloud('2')
                dictate('LED is blinking.')
            else:
                sorry()
#Kill program
        elif "quit" in menu:
            if privilege == 1:
                dictate('Are you sure?')
                while True:
                    killprogram = raw_input(">").lower()
                    if "yes" in killprogram:
                        sys.exit()
                    elif "no" in killprogram:
                        dictate('Very good, sir.')
                        break
                    else:
                        dictate('I do not understand.')
                        dictate('Do you still want to quit, sir?')
            else:
                dictate('You are not allowed to do that, '+name+'.')
                
#Random
        elif "about you" in menu or "about yourself" in menu:
            dictate('Ask me anything, '+name+'.')
        elif "hey" in menu and "butt" in menu:
            wrong()     
        else:
            sorry()
            
#login
while True:
    dictate("Hello, what is your name?")
    username = raw_input(">")
    if username == "Eric":
        privilege = 1
        name = "sir"
    else:
        privilege = 2
        name = username
    main()
