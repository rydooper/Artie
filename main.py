from AI.base import initialise
import datetime as dt
import pyjokes
import time
import subprocess

artie = initialise()

# user login will go here
#inputType: int = artie.choose_input() <- if user has previously logged in/exists, will use the Input from db
inputType: int = 1

now = dt.datetime.now()
artie.speak("Today is " + str(now.strftime("%d-%m")) + " and it is " + str(now.strftime("%H:%M")))
artie.speak("How can I help you?")

takingQueries = True
while takingQueries:
    if inputType == 1:
        try:
            query: str = input("> ").lower()
        except (KeyboardInterrupt, EOFError) as e:
            artie.speak("Keyboard input error,", e, " shutting down!")
            break
    elif inputType == 2:
        query: str = artie.takeCommand().lower()
    else:
        print("Input type: ", inputType)
        artie.speak("Invalid input detected, exiting!")
        break

    responseAgent = 'aiml'
    answer: str = artie.kernel.respond(query)
    print(answer)
    answered = False

    if answer[0] != "#":
        artie.speak(answer)
    if answer[0] == "#":
        params: list[str] = answer[1:].split("$")
        command = int(params[0])

        if command == 0:
            artie.speak(params[1])
            break

        elif command == 2:
            # tells a joke from python jokes library
            artie.speak(pyjokes.get_joke())

        elif command == 3:
            # wikipedia function
            artie.check_wiki(params[1])

        elif command == 4:
            # spotify function
            artie.speak("Spotify not fully implemented - this will be a feature in the next version!")

        elif command == 5:
            artie.check_weather()
            
        elif command == 6:
            # time function
            strTime = dt.datetime.now().strftime("%H:%M")
            artie.speak(f"The time is {strTime}")

        elif command == 7:
            # lock computer function
            artie.speak("Device locking features temporarily disabled.")
            # this needs fixing~! #can't find winll in ctypess
            # ctypes.winll.user32.LockWorkStation()
            
        elif command == 8:
            # shutdown PC function
            artie.speak("Shutting down the computer now.")
            subprocess.call('shutdown /p /f')

        elif command == 31:
            # LOGIC - "I know that * is *" statements
            # knowledge(artie, params)
            print("knowledge to be implemented")

        elif command == 32:
            # LOGIC - "check that * is *" - statements
            # knowledge_check(artie, params)
            print("knowledge_check to be implemented")

        elif command == 97:
            # stop listening
            artie.speak("I will now stop listening for 10 seconds")
            time.sleep(10)
            artie.speak("I am listening again now!")
        elif command == 98:
            # closes the program down
            artie.speak("Closing program down now, goodbye!")
            takingQueries = False
        elif command == 99:
            # checks the knowledge.csv file and compares against knowledge given using tfidf and cosine
            # tfidf_calculation(artie, query)
            print("tfidf_calculation to be implemented")
    artie.speak("Goodbye")
    artie.saveBrain(brainfile="AI/knowledge/brain/artie_brain.brn")