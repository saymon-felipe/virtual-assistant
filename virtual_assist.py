import speech_recognition as sr
import playsound 
#from gtts import gTTS
import random
import pyttsx3
import sys
sys.path.insert(1, './controllers')
import assistant_functions

class VirtualAssist():
    def __init__(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name

        self.engine = pyttsx3.init(driverName='sapi5')
        self.r = sr.Recognizer()

        self.engine.setProperty('rate', 150)

        self.voice_data = ""
        self.firstTime = True

    def engine_speak(self, text):
        print(self.assist_name + ":", text)
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def repeatRecord(self):
        self.record_audio()
        self.response(self.voice_data)

    def record_audio(self):
        self.voice_data = ""
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            playsound.playsound("assets/sounds/speak_sound.mp3")
            print("Ouvindo...")
            audio = microfone.listen(source, 5, 5)

            try:
                self.voice_data = microfone.recognize_google(audio, language='pt-BR')
                print(">> ", self.voice_data.lower())
            except sr.UnknownValueError:
                self.speak_unrecognized()
                self.repeatRecord()
            except sr.RequestError:
                self.engine_speak("Desculpe chefe, meu sistema caiu")
                self.repeatRecord()

            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def speak_unrecognized(self):
        self.engine_speak(f"Desculpe {self.person}, não entendi, pode repetir por favor?")
        
    def check_if_assistant_is_required(self):
        self.voice_data = ""
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            
            if self.firstTime:
                playsound.playsound("assets/sounds/speak_sound.mp3") 
                self.firstTime = False
                
            audio = microfone.listen(source, timeout=None, phrase_time_limit=2)
            try:
                self.voice_data = microfone.recognize_google(audio, language='pt-BR')
                print(">> ", self.voice_data)
                if self.there_exist(['ei darling', 'Hey darling', 'Olá']):
                    greetings = [f'Oi {self.person}, o que você quer fazer hoje?',
                            f'Opa {self.person}, como eu posso te ajudar?',
                            f'Salve {self.person}, o que você precisa?']
                    greet = greetings[random.randint(0, len(greetings) - 1)]
                    self.engine_speak(greet)
                    self.initAssistant()
            except sr.UnknownValueError:
                return

    #def engine_speak(self, audio_string):
       # print(self.assist_name + ":", audio_string)
       # audio_string = str(audio_string)
       # tts = gTTS(text = audio_string, lang='pt-BR', slow=False)
       # r = random.randint(1, 20000)
       # audio_file = "audio" + str(r) + ".mp3"
       # tts.save(audio_file)
        
       # playsound.playsound(audio_file)
       # os.remove(audio_file)

    def there_exist(self, terms):
        for term in terms:
            if term.lower() in self.voice_data.lower():
                return True

    def response(self, voice_data):
        playsound.playsound("assets/sounds/search_sound.mp3")
        if self.there_exist(['procure por']) and 'youtube' not in voice_data:
            search_term = voice_data.split("por")[-1]
            self.engine_speak("o que eu encontrei para " + search_term + " no google foi")
            assistant_functions.searchInInternet(search_term=search_term, youtube=False)
            return

        if self.there_exist(['procure por']) and 'youtube' in voice_data:
            search_term = voice_data.split("por")[-1]
            self.engine_speak("o que eu encontrei para " + search_term + " foi")
            assistant_functions.searchInInternet(search_term=search_term, youtube=True)
            return
        
        if self.there_exist(['entre no meu trabalho']):
            self.engine_speak("Entrando no trabalho")
            assistant_functions.open_work()
            return
        
        if self.there_exist(['bom dia']):
            currentWeather = assistant_functions.good_morning()
            self.engine_speak(f"Bom dia {self.person}, {currentWeather}, aproveite o seu dia!")
            return
    
        if self.there_exist(['adeus']):
            self.engine_speak(f"Ok {self.person}, tenha um bom dia!")
            return
        
        playsound.playsound("assets/sounds/error_sound.mp3")
        self.repeatRecord()

    def initAssistant(self):
        self.record_audio()
        self.response(self.voice_data)

assistent = VirtualAssist("Ana", "Saymon")

while True:
    assistent.check_if_assistant_is_required()
    

    
