import speech_recognition as sr
from SpeakerIdentification.predictSpeaker import voice_identification

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit = 20)  
    try:
        command = r.recognize_google(audio).lower()
        print("you said: " + command)
        file1 = open("myfile.txt", "a")  # append mode 
        file1.write('\n'+'\n'+ command) 
        file1.close() 
        with open('speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
        
        voice_identification()
      
    except sr.UnknownValueError:
        print("Sorry, Cant understand, Please say again")

#myCommand()