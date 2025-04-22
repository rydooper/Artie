import pyttsx3
import speech_recognition as sr
import aiml
import os
import wikipedia
from AI.API_funcs import get_weather

class AI:
    def __init__(self):
        self.name = "Artie"
        self.engine = pyttsx3.init()
        self.voice = self.setupVoice(self.engine)
        self.kernel = self.setupKern()
    
    def setupVoice(self, engine):
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
    
    def setupKern(self) -> aiml.Kernel:
        kern = aiml.Kernel()
        kern.setTextEncoding(None)
        if os.path.isfile("AI/knowledge/brain/artie_brain.brn"):
            kern.bootstrap(brainFile = "AI/knowledge/brain/artie_brain.brn")
        else:
            kern.bootstrap(learnFiles = "AI/knowledge/basics-aiml.xml")
            kern.saveBrain("AI/knowledge/brain/artie_brain.brn")
        return kern
    
    def saveBrain(self, brainfile):
        self.kernel.saveBrain(brainfile)

    def choose_input(self) -> int:
        self.speak("Do you wish to use keyboard [1] or microphone [2] to interact? Please input the number on keyboard to continue.")
        inputType = input("> ")
        if inputType == "1":
            self.speak("Keyboard selected, please continue.")
        elif inputType == "2":
            self.speak("Microphone selected, please continue.")
        return inputType
    
    def speak(self, audio):
        self.engine.say(audio)
        print(audio)
        self.engine.runAndWait()

    def introduce_self(self):
        self.speak("Greetings, I am " + self.name)

    def takeCommand(self, loggedInUser) -> str:
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=loggedInUser.micIndex)
        with mic as source:
            print("Listening!")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognising")
            query = r.recognize_google(audio, language="en-UK")
            print("User said: ")
            print(query, "\n")
        except Exception as e:
            print(e)
            print("Unable to recognise, sorry")
            return "none"
        return query
    
    def check_wiki(self, query):
        query = query.replace("wikipedia", "")
        self.speak("Checking wikipedia for " + query)
        results = wikipedia.summary(query, sentences=3)
        self.speak("According to Wikipedia: ")
        self.speak(results)

    def check_weather(self):
        self.speak("Please input the city you want the weather for?")
        cityName = self.takeCommand().lower()
        if cityName == None:
            self.speak("Unable to get city name, please try again.")
            return
        self.speak("Checking weather for " + cityName)
        weatherDescr = get_weather(cityName)
        self.speak(weatherDescr)

def initialise():
    artie = AI()

    artie.introduce_self()
    return artie