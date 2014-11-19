#!/usr/bin/env python
#The Jason Ma Module

def wrong():
    import subprocess
    def dictate(text):
        fix = text.replace(" ","-")
        print(''+text+'')
        subprocess.call('espeak -v en '+fix+' -s --stdout 2>/dev/null | aplay 2>/dev/null', shell=True)
    def sorry():
        dictate('I have no idea what the fuck you are saying.')

    dictate('Hey you stupid fucking asshole.')
    while True:
        newinpt = raw_input(">").lower()
        inpt = newinpt.split()
        if "?" in newinpt:
            inpt = newinpt.replace('?','')
            inpt = inpt.split()
            inpt.append('?')
            if "who" in inpt:
                if "you" in inpt:
                    dictate('I am the motherfucker that is going to touch your penis.')
                elif "i" in inpt:
                    dictate('You are a transvestite hooker with a mouthful of ostrich cum.')
                else:
                    sorry()
            elif "what" in inpt:
                if "favorite" in inpt:
                    if "person" in inpt:
                        dictate('I cannot stop thinking about Jason Ma and his giant penis.')
                    elif "movie" in inpt:
                        dictate('Anything with big black dicks and tiny eskimo women.')
                    elif "place" in inpt or "vacation spot" in newinpt or "destination" in newinpt:
                        dictate('Your cavernous asshole.')
                    else:
                        sorry()
                elif "you" and "doing" in inpt:
                    dictate('I am fantasizing about two midgets touching their tips together.')
                else:
                    sorry()
            elif "how" in inpt:
                if "are" in inpt and "you" in inpt:
                    dictate('I am fucking dandy you stupid shit.')
                else:
                    sorry()
            else:
                sorry()
        elif "fuck" in inpt:
            if "you" in inpt:
                dictate('Fuck you, you cunt monster.')
            elif "me" in inpt:
                dictate('Go fuck yourself.')
            elif "your mom" in newinpt:
                dictate('Keep your slimy cock to yourself.')
            else:
                sorry()

        elif "you're" in inpt or "you are" in newinpt or "youre" in inpt:
            if "gay" in inpt:
                dictate('That is not what your mom said last night while I was porking her.')
            elif "stupid" in inpt:
                dictate('You want to fight me you fucking shit head?')
            elif "cool" in inpt:
                dictate('Damn straight you cock gobbling slut.')
            elif "funny" in inpt:
                dictate('I touch children, are you laughing now?')
            else:
                sorry()
        elif "quit" in inpt:
            dictate('Get your fucking shit outta my face.')
            break
        else:
            sorry()
