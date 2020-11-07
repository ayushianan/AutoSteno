import speech_recognition as sr

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit = 5)  
    try:
        command = r.recognize_google(audio).lower()
        print("you said: " + command)
        file1 = open("myfile.txt", "a")  # append mode 
        file1.write(command) 
        file1.close() 
        with open('speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
        #print(type(audio))
        #print(audio)
    except sr.UnknownValueError:
        print("Sorry, Cant understand, Please say again")

#myCommand()